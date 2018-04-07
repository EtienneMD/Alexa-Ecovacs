from __future__ import print_function
from time import sleep
from datetime import datetime
from sucks import *
import os

def build_api():
    config = {
                'device_id': EcoVacsAPI.md5(str(time.time())),
                'email': os.environ['email'],
                'password': EcoVacsAPI.md5(os.environ['password']),
                'country': os.environ['country'],
                'continent': os.environ['continent']
             }

    api = EcoVacsAPI(config['device_id'],config['email'],config['password'],
                                config['country'],config['continent'])
    vac_id = api.devices()[0]
    vacbot = VacBot(api.uid,api.REALM,api.resource, api.user_access_token, vac_id, config['continent'])
    return vacbot

def perform_action(action):
    vacbot = build_api()
    vacbot.connect_and_wait_until_ready()
    vacbot.run(action)
    vacbot.disconnect()

def perform_service():
    vacbot = build_api()
    vacbot.connect_and_wait_until_ready()
    vacbot.run(Move('turn_around'))
    sleep(2)
    vacbot.run(Move('forward'))
    vacbot.disconnect()

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(card, speech_output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': speech_output
        },
        'card': card,
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }

def build_simple_card(output):
    card = {
            'type': 'Simple',
            'title': "Ecovacs",
            'content': output
    }
    return card

def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }

# --------------- Functions that control the skill's behavior ------------------

def get_clean_response():
    speech_output = "Your vaccum is starting its cleaning session."
    now = datetime.now()
    card_output = "Cleaning session started on "
    card_output += now.strftime("%B %d")
    if now.day % 10 == 1:
        card_output += "st "
    elif now.day % 10 == 2:
        card_output += "nd "
    elif now.day % 10 == 3:
        card_output += "rd "
    else:
        card_output += "th "
    card_output += (now.strftime("at %I:%M %p.")).lower()
    card = build_simple_card(card_output)
    should_end_session = True
    return build_response(None, build_speechlet_response(
        card, speech_output, None, should_end_session))

def get_charge_response():
    speech_output = "Your vaccum is going back to its station."
    should_end_session = True
    return build_response(None, build_speechlet_response(
        None, speech_output, None, should_end_session))

def get_stop_response():
    speech_output = "Your vacuum is stopping."
    should_end_session = true
    return build_response(None, build_speechlet_response(
        None, speech_output, None, should_end_session))

def get_service_response():
    speech_output = "Your vacuum is ready for some servicing."
    should_end_session = True
    return build_response(None , build_speechlet_response(
        None, speech_output, None, should_end_session))

def get_welcome_response():
    session_attributes = {}
    speech_output = "Welcome to the Ecovacs skill. What can I help you with? "
    reprompt_text = "You can ask for your vacuum to start cleaning, come out for service" \
                    "or go back to its charging station."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        None, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    speech_output = "Thank you for trying the Ecovacs skill. " \
                    "Have a nice day! "
    should_end_session = True
    return build_response({}, build_speechlet_response(
        None, speech_output, None, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()

def on_intent(intent_request, session):
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "CleanIntent":
        perform_action(Clean())
        return get_clean_response()
    elif intent_name == "EdgeIntent":
        perform_action(Edge())
        return get_clean_response()
    elif intent_name == "StopIntent":
        perform_action(Stop())
        return get_stop_response()
    elif intent_name == "ChargeIntent":
        perform_action(Charge())
        return get_charge_response()
    elif intent_name == "ServiceIntent":
        perform_service()
        return get_service_response()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")

def on_session_ended(session_ended_request, session):
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

# --------------- Main handler ------------------

def lambda_handler(event, context):
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if 'applicationId' in os.environ:
        if (event['session']['application']['applicationId'] !=
                os.environ['applicationId']):
            raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

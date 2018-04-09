# Alexa-Ecovacs
Alexa skill to interact with your Ecovacs vacuum.

# Commands
The skill has the following features:
* Clean - Starts an automatic cleaning session
* Edge - Starts an edge cleaning session
* Stop - Stops your vacuum
* Charge - Sends your vacuum back to its charging station
* Service - Tells your vacuum to turn around and move forward a few feet  
(useful if your vacuum is charging under a couch like mine is)

### Examples
* Alexa, ask my vacuum to start cleaning.
* Alexa, tell my vacuum to cleaning around the room.
* Alexa, ask my vacuum to stop.
* Alexa, ask my vacuum to go back to its charger.
* Alexa, tell my vacuum it needs to be emptied.

# Installation

## Skill creation
1. Create a new custom skill in the Amazon developer console.
2. Under Interaction Model, go to JSON Editor and use the provided interaction.json file.
3. Under Endpoint, select AWS Lambda. You will then find your Skill ID.
4. When you have created your lambda function, go back to Endpoint and enter your Lambda ARN under default region.

## Lambda deployment
1. Create a new python3.6 lambda function. Notice your Lambda ARN at the top of the page.
2. Under Designer, select Alexa Skills Kit as a trigger.
3. Under Function code, select Upload .ZIP file and use the provided Deploy.zip file.
4. Under Function code, set Handler to skill.lambda_handler.
5. Under Basic settings, set Timeout to 15 seconds.
6. Under Environment variables, define variables as described below.

## Environment variables
### Required
* **email** : Your Ecovacs login email.
* **password** : Your Ecovacs login password.
* **country** : Your two-letter country code.
* **continent** : Your two-letter continent code.
### Optional
* **applicationId** : Your Alexa skill ID.  
(Prevents unauthorized access to your skill)
* **timezone** : Your time zone. (i.e. America/Montreal, Europe/Amsterdam or Australia/Sydney)  
(Adds a card in the Alexa app to log your cleaning session)

# Development
Want to contribute? Let me know! This is my first GitHub project, I'd love to hear how to make it better.

# Thanks
This has only been made possible thanks to the amazing work of @wpietri and his [Sucks](https://github.com/wpietri/sucks) library.

# License
MIT

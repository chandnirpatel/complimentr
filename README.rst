Welcome to complimentr! This is a cute app that sends you a text message
with a compliment randomly throughout the day.

# Manual Steps
0. pip install complimentr
1. create a twilio account
2. run `complimentr`
3. input twilio account details when prompted (or save twilio details as environment variables )
  * export TWILIO_ACCOUNT_SID=ACKE...
  * export TWILIO_AUTH_TOKEN=dwjen2...
  * export FROM_PHONE="+18009898..."
  * export TO_PHONE="+180023356..."

and you will get awesome text messages throughout the day.


# Deploy to Heroku
If you would like to keep getting compliments even when you've turned off your computer
then I recommend deploying this app for free on Heroku.

* Set up a Heroku account (a free account is fine)
* Install Heroku command line tool (brew install heroku)
* `heroku login`
* Clone this repository and cd to the project root folder
* Run `heroku create`
* Set the 4 environment variables described above using `heroku config:set TWILIO_ACCOUNT_SID=ACKE...`
* git push heroku master

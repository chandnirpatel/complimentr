import os

from complimentr.ask_user_for_info import askForSettings

def get_account_sid():
    return os.environ.get(
        'TWILIO_ACCOUNT_SID',
        askForSettings("Twilio Account ID: "))

def get_account_auth_token():
    return os.environ.get(
        'TWILIO_AUTH_TOKEN',
        askForSettings("Twilio AUTH_TOKEN: "))

def get_to_phone_number():
    to_phone = os.environ.get(
        'TO_PHONE',
        askForSettings("To Phone Number: "))
    return formatAsPhoneNumber(to_phone)

def get_senders_phone_number():
    from_phone = os.environ.get(
        'FROM_PHONE',
        askForSettings("From Phone Number: "))
    return formatAsPhoneNumber(from_phone)

def formatAsPhoneNumber(userInput):
    phoneNumber = str(userInput)
    if(len(phoneNumber) < 7):
        print("Invalid phone number, please run complimentr again")
        return
    elif(len(phoneNumber) == 7):
        area_code = askForSettings("Area Code:")
        phoneNumber = area_code + phoneNumber
    elif(len(phoneNumber) == 10):
        phoneNumber = "+1" + phoneNumber
    elif(len(phoneNumber) == 11):
        phoneNumber = "+" + phoneNumber

    return phoneNumber

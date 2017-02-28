from complimentr.messageSender import sendCompliment
import time

def runComplimentrApp ():
  print("Welcome to complimentr! \n You will need set up a Twilio Account before using this app")
  compliment_count = 0
  while (compliment_count <= 10):
      time.sleep(5)
      sendCompliment()

  print("Compliment sent!")
  return

from complimentr.messageSender import sendCompliment
import time
import numpy as np

def runComplimentrApp ():
  print("Welcome to complimentr! \n You will need set up a Twilio Account before using this app")
  compliment_count = 0
  while (compliment_count <= 10):
      sendCompliment()
      waitForOnAverage6Hours()
      compliment_count = compliment_count + 1

  print("Compliment sent!")
  return

def waitForOnAverage6Hours():
    sleep_time = np.random.normal(5, 5)
    if (sleep_time <=1):
      sleep_time = 1

    time.sleep(sleep_time)
    return

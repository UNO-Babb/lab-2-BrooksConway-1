#FutureTime.py
#Name: Brooks Conway
#Date: 1/29/25
#Assignment: Future Time Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  #TODO:
  #Ask user for hours
  hours = input("Enter hours: ")
  hours = int(hours)
  futurehour = currentHour + hours
  futurehour = futurehour % 24
  print(futurehour)
  #Ask user for minutes
  minutes = input("Enter minutes: ")
  minutes = int(minutes)
  futuremin = currentMinute + minutes
  futuremin= futuremin % 60
  print(futuremin)
  #Calculate the time after the user-supplied time has passed.
strHour = str(futurehour)
strMin = str(futuremin)
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
print(strHour , ":" , strMin)

if __name__ == '__main__':
  main()

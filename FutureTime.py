#FutureTime.py
#Name: Brooks Conway
#Date: 1/29/25
#Assignment: Future Time Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  print(main)
now = datetime.datetime.now()
currentHour = (now.hour - 6) % 24
currentMinute = now.minute

hours = input("Enter hours: ")
hours = int(hours) #convert to number

mins = input("Enter mins: ")
mins = int(mins)

extraHour = (currentMinute + mins) // 60
futureMin = (currentMinute + mins) % 60

futureHour = (currentHour + hours + extraHour) % 24

strHour = str(futureHour)
strMin = str(futureMin)

print(strHour + ":" + strMin)
if __name__ == '__main__':
  main()

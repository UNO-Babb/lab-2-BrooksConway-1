#Magic8Ball.py
#Name:Brooks Conway
#Date:1/29/25
#Assignment: Magic Eight Ball (Lab 2)

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")

  answers=["As I see it, yes." , "Ask again later." , "Better not tell you now." , "Cannot predict now." , "Concentrate and ask again." , "Don’t count on it." , "It is certain." , "My reply is no." , "My sources say no." , "Outlook not so good."]
  #Prompt the user for their question.
  question = input("Ask me a question: ")
  #Answer question randomly with one of the options from your earlier list.
  num= random.random()
  num = num * 1000
  num = int(num)
  things = len(answers)
  num = num % things
  print(answers[num])
if __name__ == '__main__':
  main()

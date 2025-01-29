#Magic8Ball.py
#Name: Kalia
#Date: 29Jan25
#Assignment: Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
answers = ["Yes ", "NO ", "Maybe ", "Definitely ", "Possibly ", "Absolutely Not" ]
  #Answer question randomly with one of the options from your earlier list.
num = random.random() #decimal 0-1
num = num * 1000 #decimal 0-999
num = int(num) #no more decimals
num = num % 6 #0-19
#things is the length of questions
#things = len(answers)
#num = num % things
print(random.choice(answers))


question = input("Ask me a question: ")
print(answers[num])



if __name__ == '__main__':
  main()

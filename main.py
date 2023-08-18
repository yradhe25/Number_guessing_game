import random

def rules():
  print("Welcome to the Number Guessing Game!")
  print("The rules are as follows :")
  print("You need to guess a random number between 1 and 100.")
  print("You have 10 guesses to find the correct number.")
  print("If your guess is too low, I'll let you know it's 'Too low'.")
  print("If your guess is too high, I'll let you know it's 'Too high'.")
  print("You can also enter -1 to quit the game.")
  print("Let's begin!")

def takeInput():
  number = random.randint(1, 100)
  noOfGuesses=10
  
  while(True):
    print(f"Remaining guesses = {noOfGuesses}")
    userInput1 = input("Pick a number between 1 and 100 or Enter -1 to quit : ")
    
    try:
      userInput = int(userInput1)
    except ValueError:
      print("Please enter a valid number between 1 and 100!")
      continue
    noOfGuesses -= 1
    
    if noOfGuesses==0:
      print("You lost!")
      print(f"The number was {number}")
      again=input("Do you want to play again? ( Y/N ) : ")
      
      while not (again.upper()=="Y" or again=="N"):
        print("Enter a valid choice")
        again=input("Do you want to play again? ( Y/N ) : ")
     
      if again.upper()=="Y":
        takeInput()
     
      elif again.upper()=="N":
        print("Thank You for playing the game. Goodbye!") 
        break
      break
    
    if (userInput == number):
      print("Congratulations! You won")
      print(f"The number was {number}")
      again=input("Do you want to play again Y/N : ")
     
      while not (again.upper()=="Y" or again.upper()=="N"):
        print("Enter a valid choice")
        again=input("Do you want to play again Y/N : ")
     
      if again.upper()=="Y":
        takeInput()
     
      elif again.upper()=="N":
        print("Thank You for playing the game. Goodbye!")
        break
      break
   
    elif (userInput > 0 and userInput <= 100 and userInput < number):
      print("Too low")
  
    elif (userInput > 0 and userInput <= 100 and userInput > number):
      print("Too high")
   
    elif (userInput==-1):
      print("Thank You for playing the game. Goodbye!")
      break
   
    else:
      print("Please enter a valid number between 1 and 100!")

rules()
takeInput() 
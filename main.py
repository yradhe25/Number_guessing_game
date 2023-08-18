import random

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
      again=input("Do you want to play again? ( Y/N ) : ")
      
      while not (again=="Y" or again=="y" or again=="N" or again=="n"):
        print("Enter a valid choice")
        again=input("Do you want to play again? ( Y/N ) : ")
     
      if again=="Y" or again=="y":
        takeInput()
     
      elif again=="N" or again=="n":
        print("Thank You for playing the game. Goodbye!") 
        break
      break
    
    if (userInput == number):
      print("Congratulations! You won")
      print(f"The number was {number}")
      again=input("Do you want to play again Y/N : ")
     
      while not (again=="Y" or again=="y" or again=="N" or again=="n"):
        print("Enter a valid choice")
        again=input("Do you want to play again Y/N : ")
     
      if again=="Y" or again=="y":
        takeInput()
     
      elif again=="N" or again=="n":
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

takeInput()
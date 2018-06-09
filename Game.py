import sys                                                                   # Importing required packages
import random
import time

def game(user, choice):                              # Defining a function which will accept 2 inputs from user as (user, choice)
	choice = str(input(user + ", What's your choice?: "))      # Choice will accept value Rock/ Paper/ Scissors
	opt = ["Rock", "Paper", "Scissors"]                        # opt is a list of values
	bot = random.choice(opt)                                   # bot will contain random values from opt
	time.sleep(1)                                              # Delayed output by 1 second
	if choice == "Rock" and bot == "Scissors":                        # If else statements nested within
		print (user + ", you WON !! as bot chose scissors")
	elif choice == "Rock" and bot == "Paper":
		print (user + ", you LOSE !! as bot chose paper")
	elif choice == "Paper" and bot == "Scissors":
		print (user + ", you LOSE !! as bot chose scissors")
	elif choice == "Paper" and bot == "Rock":
		print (user + ", you WON !! as bot chose rock")
	elif choice == "Scissors" and bot == "Paper":
		print (user + ", you WON !! as bot chose paper")
	elif choice == "Scissors" and bot == "Rock":
		print (user + ", you LOSE !! as bot chose rock")
	elif choice == bot:
		print ("It's a TIE !!")
	elif choice not in opt:                                     # if choice of user is not in opt then return invalid input
		print ("Oh NO !! Invalid input. Choose only from <Rock/Paper/Scissors>")
		
def start():                                                       # Defining a function start to make game little more interactive
	while True:
		user = str(input("What's your name?: "))           # User's name will be contained here
		choice = ""                                        # Passing choice empty
		print (game(user, choice))                         # game() will run in this block
		while True:                                        # While loop so user will be propted to play again
			x = input(user + " , Do you want to play again ? Type Y/N: ")  # Accepting value from user as Yes/No
			if x == "Y":                               # if value is Y restart the game with same user
				print (game(user, choice))
			elif x == "N":                             # if value is N then exit the game
				print ("Goodbye " + user)
				sys.exit()
			else:                                      # if user passes value other than Y/N prompt him with Invalid Input
				print ("Invalid Input")
				
print (start())                                                    # Run the Game

# CODED BY - GAURAV PADAWE

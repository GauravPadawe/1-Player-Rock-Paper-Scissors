import sys
import random
import time

def game(user, choice):
	choice = str(input(user + ", What's your choice?: "))
	opt = ["Rock", "Paper", "Scissors"]
	bot = random.choice(opt)
	time.sleep(1)
	if choice == "Rock" and bot == "Scissors":
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
	elif choice not in opt:
		print ("Oh NO !! Invalid input. Choose only from <Rock/Paper/Scissors>")
		
def start():
	while True:
		user = str(input("What's your name?: "))
		choice = ""
		print (game(user, choice))
		while True:
			x = input(user + " , Do you want to play again ? Type Y/N: ")
			if x == "Y":
				print (game(user, choice))
			elif x == "N":
				print ("Goodbye " + user)
				sys.exit()
			else:
				print ("Invalid Input")
				
print (start())
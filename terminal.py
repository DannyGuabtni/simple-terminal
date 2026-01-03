from rich import print as rprint
import random
import json

def terminal():
	running = True
	rprint("[bold blue]Welcome to the terminal![/] Enter 'help' for a list of commands.", end = "")
	while running:
		user_command = input(" > ").lower()
		while user_command not in ("help", "number game", "calculator", "quit", "wordle"):
			user_command = input("Invalid input, please try again. > ").lower()
		if user_command == "number game":
			number_game()
		elif user_command == "calculator":
			calculator()
		elif user_command == "wordle":
			wordle()
		elif user_command == "help":
			print(
				"'help': Return this list of useful commands.\n"
				"'number game': Start a game where you guess a number between 1 and 100.\n"
				"'calculator': Input two numbers and an operator to get a result.\n"
				"'quit': Exit the terminal.\n"
				"'wordle': Guess a five-letter word in 6 tries or less."
				)
		elif user_command == "quit":
			break

def check_restart():
	keep_playing = input("[y/n] > ").lower()
	while keep_playing not in ("y","n"):
		keep_playing = input("Invalid input, please try again. [y/n] > ").lower()
	if keep_playing == "n":
		rprint("[bold blue]Exiting program...[/]")
		return False
	elif keep_playing == "y":
		rprint("[bold blue]Restarting program...[/]")
		return True

def number_game():
	playing = True
	while playing == True:
		random_num = random.randint(1,100)
		user_num = int(input("Guess the hidden number from 1 to 100 > "))
		count = 1
		while user_num != random_num:
			if user_num > random_num:
				rprint("[bold blue]Lower![/]", end = "")
			if user_num < random_num:
				rprint("[bold yellow]Higher![/]", end = "")
			user_num = int(input(" > "))
			count += 1
		if count == 1:
			rprint(f"[bold green]Wow![/] You managed to get the mystery number {random_num} in just 1 try, you lucky duck! Want to play again?", end = "")
		else:
			rprint(f"[bold green]Congrats![/] You managed to guess the mystery number {random_num} in {count} tries! Want to play again?", end = "")
		playing = check_restart()

def calculator():
	playing = True
	while playing == True:
		num_1 = int(input("Enter first number > "))
		op = input("Enter operator [+, -, *, /] > ")
		num_2 = int(input("Enter second number > "))
		while op not in ("+", "-", "*", "/"):
			rprint(f"[bold red]Error detected[/]: operator {op} invalid. Try entering the operator again", end = "")
			op = input("Enter operator [+, -, *, /] > ")
		if op == "+":
			result = num_1 + num_2
		elif op == "-":
			result = num_1 - num_2
		elif op == "*":
			result = num_1 * num_2
		elif op == "/":
			result = num_1 / num_2
		rprint(f"The result is [bold blue]{result}[/]. Would you like to calculate again?", end = "")
		playing = check_restart()

def validate_answer(answer, guess):
	# Initialise result as grey 5 times
	result = ["grey"] * 5
	guess_letters = list(guess)
	answer_letters = list(answer)
	# Check for greens
	for i in range(5):
		if guess_letters[i] == answer_letters[i]:
			result[i] = "green"
			answer_letters[i] = None
	# Check for yellows
	for i in range(5):
		if result[i] == "grey" and guess_letters[i] in answer_letters:
			result[i] = "yellow"
			answer_letters[answer_letters.index(guess_letters[i])] = None
	# Initialise validated answer as an empty dictionary
	validated = []
	for i in range(5):
		validated.append((guess_letters[i], result[i]))
	return validated

def print_validated_answer(validated):
	for letter, colour in validated:
		rprint(f"[{colour}]{letter}[/]", end = " ")
	print()

def wordle():
	playing = True
	while playing == True:
		count = 1
		answer = random.choice(words).upper()
		guess = None
		while guess != answer and count < 6:
			guess = input("> ").upper()
			count += 1
			validated = validate_answer(answer,guess)
			print_validated_answer(validated)
		if guess != answer:
			rprint(f"[bold red]Game over![/] You failed to guess the mystery word [bold blue]{answer}[/] in 6 tries or less! Want to play again?")
		else:
			rprint(f"[bold green]Congrats![/] You successfully guessed the mystery word [bold blue]{answer}[/] in 6 tries or less! Want to play again?")
		playing = check_restart()

# Start main program and load words.json (only needs to happen once)
with open("words.json", "r") as file:
	word_dict = json.load(file)
	words = word_dict["words"]

terminal()
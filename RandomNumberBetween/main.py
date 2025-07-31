# Initialize variables and game state.
# Expected Imports
from random import randint
    # random number generator
game_exit = False
guess_history = {0:0}
random_number = 0
valid_input = False
init_prompt = (input("Please hit enter to start the game."))
guess_value = 0 
loop_count = 0
while game_exit == False:
    if loop_count == 0:
        winning_value = randint(1,100)
        print(f"The random number {winning_value} has been generated.")
    else:
        pass
    guess_value = int(input("Please enter a number between 1 and 100 : "))
    print(f"loop {loop_count} started")
    guess_history[loop_count] = guess_value
    print(f"new loop history {guess_history}")

    if guess_value == winning_value:
        print(f"Yon won by guessing {winning_value} in {len(guess_history)} guesses")
        game_exit = True
    elif 100 >= guess_value > winning_value:
        print("You are guessing too high, guess again.")
    elif 0 < guess_value < winning_value:
        print("You are guessing too low, guess again.")
    else:
        print('INVALID ENTRY, please type and integer followed by the enter key')
    loop_count+=1
    print (f"{guess_history}")


# Expected Helper Function // Nice to Have, save for later
#Expected Data Types22
    # int : Random Number
    # bool : game exit
    # int(input()) : user input number
    # bool : valid input check
    # dict : guess histor {attempt coiunt:random number guess}

# Begin a game loop until exit condition is met.
    #Generate a random number
    #Prompt user for an guess
    #Compare to value
    # Execute Approriate Case
        # Too High
        # Too Lod
        # Number Guessed

# Execute exit functionaliy
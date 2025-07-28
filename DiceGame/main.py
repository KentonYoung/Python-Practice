import math, random

print("Let's Roll Some Dice!")
button_entry = input("Press Any Button To Start")
start_game = button_entry != ""
if start_game == True:
    ## initialize game loop
    player_one=input("Please enter Player One's name ")
    player_two=input("Please enter Player Two's name ")
    player_dict={0:player_one, 1:player_two}
    quit = False
    exit_condition = False
    turn_count = 0
    player_one_rolls={0:0,1:0,2:0}
    player_two_rolls={0:0,1:0,2:0}
    player_one_score = sum(player_one_rolls.values())
    player_two_score = sum(player_two_rolls.values())
    round_numbers = {0:"First", 1:"Second", 2:"Third"}
    round_count = 0
    turn_count = 0
    
    while  (quit and exit_condition) == False:

        turn_action = input("Please type 'r', to roll the dice, or 'q' to exit the game.")
        active_player= turn_count%2
        inactive_player = (turn_count + 1)%2
        if turn_count<6:
            print(f"It is currently {player_dict.get(active_player)+" "+round_numbers[round_count]}'s turn ")
        else:
             break
        if turn_action == "r" and turn_count<6:    
                dice_roll= (random.randint(1,6)) + random.randint(1,6)
                if active_player == 0:
                    player_one_rolls[round_count]=dice_roll
                    player_one_score = sum(player_one_rolls.values())
                    print(f"Player One has so far rolled {player_one_rolls.values()}")
                    print(f"Player One's score is now {player_one_score}")
                else:
                    player_two_rolls[round_count]=dice_roll
                    player_two_score = sum(player_two_rolls.values())
                    print(f"Player Two has so far rolled {player_two_rolls.values()}")
                    print(f"Player Two's score is now {player_two_score}")
                print(dice_roll)
                if dice_roll == 2:
                    print("OOOF SNAKE EYES!")
                elif dice_roll <=5:
                    print("Sorry SHIT ROLL!")
                elif dice_roll>5 and dice_roll<12:
                    print("DAYUM!!!!")
                else :
                    print(f"BOX CARS!!!!!! good luck keeping up {player_dict.get(inactive_player)}")

        elif turn_action == "q":
                print("game quite")
                quit=True
                break
        else:
                print("INVALID ENTRY")

        if turn_count%2 !=0:
            round_count+=1
            print(f"Current Turn Count is {turn_count} ")
            print(f" Current Round Count is {round_count}")
        else:
            pass
        turn_count+=1
   
        print("game loop run")
        if (turn_count==6):
            exit_condition==True
            if player_one_score>player_two_score:
                print(f"PLAYER ONE WINS\n with a final score of {player_one_score}")
                break
            elif player_one_score == player_two_score:
                print(f"IT'S A TIE GAME!!!\n with a final score of {player_two_score}")
                break
            else:
                print(f"PLAYER TWO WINS\n with a final score of {player_two_score}")
                break
        else:
             pass    
        print(turn_count)
    print("Game Finished")
# Ultimate Battleships

def print_ships_to_be_placed():
    print("Ships to be placed:", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Ships to be placed: ")


def print_single_element(elem):
    print(str(elem), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write(str(elem) + " ")


def print_empty_line():
    print()
    if FILE_OUTPUT_FLAG:
        f.write("\n")


def print_player_turn_to_place(n):
    print("It is Player {}'s turn to place their ships.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to place their ships.\n".format(n))


def print_to_place_ships():
    print("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Enter a name, coordinates and orientation to place a ship (Example: Carrier 1 5 h) : \n")



def print_incorrect_input_format():
    print("Input is in incorrect format, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Input is in incorrect format, please try again.\n")


def print_incorrect_coordinates():
    print("Incorrect coordinates given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect coordinates given, please try again.\n")


def print_incorrect_ship_name():
    print("Incorrect ship name given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect ship name given, please try again.\n")


def print_incorrect_orientation():
    print("Incorrect orientation given, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write("Incorrect orientation given, please try again.\n")



def print_ship_is_already_placed(ship):
    print(ship, "is already placed, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " is already placed, please try again.\n")



def print_ship_cannot_be_placed_outside(ship):
    print(ship, "cannot be placed outside the board, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed outside the board, please try again.\n")



def print_ship_cannot_be_placed_occupied(ship):
    print(ship, "cannot be placed to an already occupied space, please try again.")
    if FILE_OUTPUT_FLAG:
        f.write(ship + " cannot be placed to an already occupied space, please try again.\n")


def print_confirm_placement():
    print("Confirm placement Y/N :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Confirm placement Y/N : \n")



def print_player_turn_to_strike(n):
    print("It is Player {}'s turn to strike.".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("It is Player {}'s turn to strike.\n".format(n))


def print_choose_target_coordinates():
    print("Choose target coordinates :", end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Choose target coordinates : ")


def print_miss():
    print("Miss.")
    if FILE_OUTPUT_FLAG:
        f.write("Miss.\n")



def print_type_done_to_yield(n):
    print("Type done to yield your turn to player {} :".format(n), end=" ")
    if FILE_OUTPUT_FLAG:
        f.write("Type done to yield your turn to player {} : \n".format(n))


def print_tile_already_struck():
    print("That tile has already been struck. Choose another target.")
    if FILE_OUTPUT_FLAG:
        f.write("That tile has already been struck. Choose another target.\n")


def print_hit():
    print("Hit!")
    if FILE_OUTPUT_FLAG:
        f.write("Hit!\n")



def print_player_won(n):
    print("Player {} has won!".format(n))
    if FILE_OUTPUT_FLAG:
        f.write("Player {} has won!\n".format(n))


def print_thanks_for_playing():
    print("Thanks for playing.")
    if FILE_OUTPUT_FLAG:
        f.write("Thanks for playing.\n")



def print_3d_list(my_list):
    first_d = len(my_list[0])
    for row_ind in range(first_d):
        second_d = len(my_list[0][row_ind])
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[0][row_ind][col_ind], end=' ')
        print("\t\t\t", end='')
        print("{:<2}".format(row_ind + 1), end=' ')
        for col_ind in range(second_d):
            print(my_list[1][row_ind][col_ind], end=' ')
        print()
    print("", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\t\t", end='   ')
    for row_ind in range(first_d):
        print(row_ind + 1, end=' ')
    print("\nPlayer 1\t\t\t\t\t\tPlayer 2")
    print()

    if FILE_OUTPUT_FLAG:
        first_d = len(my_list[0])
        for row_ind in range(first_d):
            second_d = len(my_list[0][row_ind])
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[0][row_ind][col_ind] + " ")
            f.write("\t\t\t")
            f.write("{:<2} ".format(row_ind + 1))
            for col_ind in range(second_d):
                f.write(my_list[1][row_ind][col_ind] + " ")
            f.write("\n")
        f.write("   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\t\t   ")
        for row_ind in range(first_d):
            f.write(str(row_ind + 1) + " ")
        f.write("\nPlayer 1\t\t\t\t\t\tPlayer 2\n")
        f.write("\n")


def print_rules():
    print("Welcome to Ultimate Battleships")
    print("This is a game for 2 people, to be played on two 10x10 boards.")
    print(
        "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).")
    print(
        "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.")
    print(
        "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.")
    print("If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.")
    print("If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.")
    print(
        "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.")
    print("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.")
    print("The last player to have an unsunk ship wins.")
    print("Have fun!")
    print()

    if FILE_OUTPUT_FLAG:
        f.write("Welcome to Ultimate Battleships\n")
        f.write("This is a game for 2 people, to be played on two 10x10 boards.\n")
        f.write(
            "There are 5 ships in the game:  Carrier (occupies 5 spaces), Battleship (4), Cruiser (3), Submarine (3), and Destroyer (2).\n")
        f.write(
            "First, the ships are placed. Ships can be placed on any unoccupied space on the board. The entire ship must be on board.\n")
        f.write(
            "Write the ship's name, followed by an x y coordinate, and the orientation (v for vertical or h for horizontal) to place the ship.\n")
        f.write(
            "If a player is placing a ship with horizontal orientation, they need to give the leftmost coordinate.\n")
        f.write(
            "If a player is placing a ship with vertical orientation, they need to give the uppermost coordinate.\n")
        f.write(
            "Player 1 places first, then Player 2 places. Afterwards, players take turns (starting from Player 1) to strike and sink enemy ships by guessing their location on the board.\n")
        f.write("Guesses are again x y coordinates. Do not look at the board when it is the other player's turn.\n")
        f.write("The last player to have an unsunk ship wins.\n")
        f.write("Have fun!\n")
        f.write("\n")


# Create the game
board_size = 10
f = open('UltimateBattleships.txt', 'w')
FILE_OUTPUT_FLAG = True

print_rules()


try:  # The entire code is in this try block, if there ever is an error during execution, we can safely close the file.



    # some useful variables
    threed_lst = [[['-' for k in range(10)] for j in range(10)] for i in range(2)]
    ships_dic = {'carrier': 5, 'battleship': 4, 'cruiser': 3, 'submarine': 3, 'destroyer': 2}
    empty_board = [['-' for k in range(10)] for j in range(10)]
    ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    # placement phase
    player_num = 1
    player_1_board = [['-' for k in range(10)] for j in range(10)]
    remaining_ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    player_1_coors = [] # player 1 ship coordinates
    while True:  # outer while loop for player 1 placements, since we need to take input indefinitely many times
        print_3d_list([player_1_board, empty_board])  # print out the board in every round
        print_ships_to_be_placed()
        for ship in [key for key in remaining_ships.keys()]:  # remaining ships
            print_single_element(ship)

        print_empty_line()

        print_player_turn_to_place(player_num)
        print_to_place_ships()
        player_input = input()  # player 1 input
        player_input = player_input.split()  # stored in a list to index easily
        if len(player_input) != 4:  # check input legality
            print_incorrect_input_format()
            continue  # if input is not correct, start the while loop again to get new input
            # for every illegal input, continue statement will be repeated
        try:
            x_coor = int(player_input[1])  # check whether input coordinates are integers
            y_coor = int(player_input[2])
        except:
            print_incorrect_input_format()
            continue
        if x_coor > 10 or x_coor < 1 or y_coor > 10 or y_coor < 1:  # check if input coordinates are inside the board
            print_incorrect_coordinates()
            continue

        try:
            ship_name = player_input[0].capitalize()  # check if input ship name is a string

        except:
            print_incorrect_ship_name()
            continue

        if ship_name not in ships.keys():  # check if input ship name is an actual ship name
            print_incorrect_ship_name()
            continue



        if player_input[3] != 'h' and player_input[3] != 'H' and player_input[3] != 'v' and player_input[3] != 'V':
            print_incorrect_orientation()  # check if input orientation is legal
            continue

        ship_or = player_input[3].lower()  # assign ship orientation

        if ship_name not in remaining_ships.keys():  # check if input ship haven't been placed yet
            print_ship_is_already_placed(ship_name)
            continue

        ship_length = remaining_ships[ship_name]  # assign ship length from remaining ships dictionary


        if (ship_or == 'h' and x_coor+ship_length > 11) or (ship_or == 'v' and y_coor+ship_length > 11):
            print_ship_cannot_be_placed_outside(ship_name)  # check if ship is placed inside the board
            continue

        if (x_coor, y_coor) in player_1_coors:
            print_ship_cannot_be_placed_occupied(ship_name)  # check if the input coordinates coincide with another ship
            continue

        ship_coors = set()
        if ship_or == 'h':
            for x in range(x_coor, x_coor + ship_length ):  # coordinates of the ship in a set if placed horizontally
                ship_coors.add((x,y_coor))

        if ship_or == 'v':
            for y in range(y_coor, y_coor + ship_length):  # coordinates of the ship in a set if placed vertically
                ship_coors.add((x_coor,y))

        player_1_coors_set = set(player_1_coors)  # player 1's ship coordinates in a set to check intersection
        if ship_coors.intersection(player_1_coors) != set():  # check if ship coors coincide with already placed ones
            print_ship_cannot_be_placed_occupied(ship_name)
            continue

        if ship_or == 'h':  # after the coincidence check, append ship coordinates to player coordinates
            for x in range(x_coor, x_coor + ship_length ):  # for horizontal placement
                player_1_coors.append((x,y_coor))

        if ship_or == 'v':
            for y in range(y_coor, y_coor + ship_length):  # for vertical placement
                player_1_coors.append((x_coor,y))


        # after all the checks are done, we can place the ships by changing the boards
        if ship_or == 'h':
            player_1_board[y_coor - 1][x_coor - 1:x_coor - 1 + ship_length] = '#' * ship_length  # place ship
            remaining_ships.pop(ship_name)  # once placed, ship is popped out of the remaining ships dic
        elif ship_or == 'v':
            for row_num in range(y_coor, y_coor + ship_length):  # place ship
                player_1_board[row_num-1][x_coor - 1] = '#'
            remaining_ships.pop(ship_name)  # once placed, ship is popped out of the remaining ships dic

        if len(remaining_ships) == 0:  # all the ships are placed
            print_3d_list([player_1_board, empty_board])  # one last board print before confirmation
            yes_flag = False  # yes_flag to break out of the outer loop if user inputs y
            while True:  # outer while loop if we have to ask multiple times
                print_confirm_placement()
                confirmation = input()  # confirmation input
                confirmation = confirmation.lower()  # lower for an easier check
                if confirmation == 'y':  # if yes, yes_flag is true
                    yes_flag = True
                    break
                elif confirmation == 'n':  # if no, reset all useful variables and start again
                    remaining_ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
                    player_1_board = [['-' for k in range(10)] for j in range(10)]
                    player_1_coors = []
                    break
                else:  # if input is not 'y' or 'n', it is illegal, so we ask again
                    continue
            if yes_flag == True:  # if user input is 'y', break out of the outer while loop
                break


    # player 2 placement phase
    # same comments I made for player 1 placement phase applies
    # reset useful variables
    empty_board = [['-' for k in range(10)] for j in range(10)]
    player_num = 2
    player_2_board = [['-' for k in range(10)] for j in range(10)]
    remaining_ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
    player_2_coors = []
    while True:
        print_3d_list([empty_board, player_2_board])
        print_ships_to_be_placed()
        for ship in [key for key in remaining_ships.keys()]:
            print_single_element(ship)

        print_empty_line()
        print_player_turn_to_place(player_num)
        print_to_place_ships()
        player_input = input()
        player_input = player_input.split()
        if len(player_input) != 4:
            print_incorrect_input_format()
            continue


        try:
            x_coor = int(player_input[1])
            y_coor = int(player_input[2])
        except:
            print_incorrect_input_format()
            continue
        if x_coor > 10 or x_coor < 1 or y_coor > 10 or y_coor < 1:
            print_incorrect_coordinates()
            continue

        try:
            ship_name = player_input[0].capitalize()

        except:
            print_incorrect_ship_name()
            continue

        if ship_name not in ships.keys():
            print_incorrect_ship_name()
            continue

        if player_input[3] != 'h' and player_input[3] != 'H' and player_input[3] != 'v' and player_input[3] != 'V':
            print_incorrect_orientation()
            continue

        ship_or = player_input[3].lower()

        if ship_name not in remaining_ships.keys():
            print_ship_is_already_placed(ship_name)
            continue

        ship_length = remaining_ships[ship_name]

        if (ship_or == 'h' and x_coor + ship_length > 11) or (ship_or == 'v' and y_coor + ship_length > 11):
            print_ship_cannot_be_placed_outside(ship_name)
            continue

        if (x_coor, y_coor) in player_2_coors:
            print_ship_cannot_be_placed_occupied(ship_name)
            continue

        ship_coors = set()
        if ship_or == 'h':
            for x in range(x_coor, x_coor + ship_length):
                ship_coors.add((x, y_coor))

        if ship_or == 'v':
            for y in range(y_coor, y_coor + ship_length):
                ship_coors.add((x_coor, y))

        player_2_coors_set = set(player_2_coors)
        if ship_coors.intersection(player_2_coors) != set():
            print_ship_cannot_be_placed_occupied(ship_name)
            continue

        if ship_or == 'h':
            for x in range(x_coor, x_coor + ship_length):
                player_2_coors.append((x, y_coor))

        if ship_or == 'v':
            for y in range(y_coor, y_coor + ship_length):
                player_2_coors.append((x_coor, y))


        if ship_or == 'h':
            player_2_board[y_coor - 1][x_coor - 1:x_coor - 1 + ship_length] = '#' * ship_length
            remaining_ships.pop(ship_name)
        elif ship_or == 'v':
            for row_num in range(y_coor, y_coor + ship_length):
                player_2_board[row_num - 1][x_coor - 1] = '#'
            remaining_ships.pop(ship_name)

        if len(remaining_ships) == 0:
            print_3d_list([empty_board, player_2_board])
            yes_flag = False
            while True:
                print_confirm_placement()
                confirmation = input()
                confirmation = confirmation.lower()
                if confirmation == 'y':
                    yes_flag = True
                    break
                elif confirmation == 'n':
                    remaining_ships = {'Carrier': 5, 'Battleship': 4, 'Cruiser': 3, 'Submarine': 3, 'Destroyer': 2}
                    player_2_board = [['-' for k in range(10)] for j in range(10)]
                    player_2_coors = []
                    break
                else:
                    continue
            if yes_flag == True:
                break

    # placement phases for both players are over
    # we move on to the battle phase
    ### battle phase
    player_1_hboard = [['-' for k in range(10)] for j in range(10)]  # boards of each player after the hits or misses
    player_2_hboard = [['-' for k in range(10)] for j in range(10)]
    player_1_hitcount = 0  # hit counts to check who wins in the end
    player_2_hitcount = 0
    while player_1_hitcount < 17 and player_2_hitcount < 17:  # outer while loop for battle phase
        turn_player_1 = True  # a boolean to decide whose turn it is, True-->player 1 False-->player 2
        while turn_player_1:  # while loop for player 1's guesses, since we ask indefinitely many times
            print_3d_list([player_1_board, player_2_hboard])  # print the boards in every guess round
            print_player_turn_to_strike(1)
            print_choose_target_coordinates()
            player_1_hcoors = input()  # take input from player 1
            player_1_hcoors = player_1_hcoors.split()
            if len(player_1_hcoors) != 2:  # check if input format is correct
                print_incorrect_input_format()

                continue  # continue statements will repeat for every illegal input
            try:
                x_hcoor = int(player_1_hcoors[0])  # check if coordinates are integers
                y_hcoor = int(player_1_hcoors[1])
            except:
                print_incorrect_input_format()
                continue
            if player_2_board[y_hcoor - 1][x_hcoor - 1] == '!' or player_2_board[y_hcoor - 1][x_hcoor - 1] == 'O':
                print_tile_already_struck()  # check if the tile is already struck
                continue

            if (x_hcoor, y_hcoor) in player_2_coors:  # hit!!!
                print_hit()
                player_2_hboard[y_hcoor - 1][x_hcoor - 1] = '!'  # change the player 2 hit board accordingly
                player_2_board[y_hcoor - 1][x_hcoor - 1] = '!'
                player_1_hitcount += 1
            else:  # miss!!!
                try:  # check if input coordinates are inside the board, if not, this try block will get an error
                    player_2_hboard[y_hcoor - 1][x_hcoor - 1] = 'O'   # change the player 2 hit board accordingly
                    player_2_board[y_hcoor - 1][x_hcoor - 1] = 'O'
                except:
                    print_incorrect_input_format()
                    continue
                print_miss()

                while True:  # while loop for yielding phase, since we may need to ask many times
                    print_type_done_to_yield(2)
                    done_inp = input()  # yield input
                    try:
                        done_inp = done_inp.lower()  # check if it is a string
                    except:
                        continue  # if not, ask again
                    if done_inp == 'done':  # if yield input is done
                        turn_player_1 = False  # it's player 2's turn so change the boolean and break
                        break
            if player_1_hitcount > 16:  # check after every guess round if player 1 has won
                print_3d_list([player_1_board, player_2_hboard])
                break

        while not turn_player_1:  # while loop for player 2's guesses, same comments I made above applies
            print_3d_list([player_1_hboard, player_2_board])
            print_player_turn_to_strike(2)
            print_choose_target_coordinates()
            player_2_hcoors = input()
            player_2_hcoors = player_2_hcoors.split()
            if len(player_2_hcoors) != 2:
                print_incorrect_input_format()
                continue
            try:
                x_hcoor = int(player_2_hcoors[0])
                y_hcoor = int(player_2_hcoors[1])
            except:
                print_incorrect_input_format()
                continue
            if player_1_board[y_hcoor - 1][x_hcoor - 1] == '!' or player_1_board[y_hcoor - 1][x_hcoor - 1] == 'O':
                print_tile_already_struck()
                continue
            if (x_hcoor, y_hcoor) in player_1_coors:  # hit
                print_hit()
                player_1_hboard[y_hcoor - 1][x_hcoor - 1] = '!'
                player_1_board[y_hcoor - 1][x_hcoor - 1] = '!'
                player_2_hitcount += 1
            else:  # miss
                try:
                    player_1_hboard[y_hcoor - 1][x_hcoor - 1] = 'O'
                    player_1_board[y_hcoor - 1][x_hcoor - 1] = 'O'
                except:
                    print_incorrect_input_format()
                    continue
                print_miss()

                while True:
                    print_type_done_to_yield(1)
                    done_inp = input()
                    try:
                        done_inp = done_inp.lower()
                    except:
                        continue
                    if done_inp == 'done':
                        turn_player_1 = True
                        break
            if player_2_hitcount > 16:
                print_3d_list([player_1_hboard, player_2_board])
                break
    if player_1_hitcount > player_2_hitcount:  # at the end, check which player has won and store the num in a variable
        winner_num = 1
    else:
        winner_num = 2
    print_player_won(winner_num) # the end of the game
    print_thanks_for_playing()


except:
    f.close()


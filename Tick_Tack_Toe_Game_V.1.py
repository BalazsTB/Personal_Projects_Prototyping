#print the board
#ask for move
#check if valid move
#update the board
#check for win condition
#move to next player
#repeat

from cmath import exp


board = [[" "," "," "],[" "," "," "],[" "," "," "]]

#def check_if_valid_move():
 #   print("Valid move")

def update_board(_coordinate_x,_coordinate_y, _player_ID):
    print("test")
    if _player_ID == 1:
        board[_coordinate_x][_coordinate_y] = "X"
    else:
        board[_coordinate_x][_coordinate_y] = "Y"

def print_board():
    print("      1   " + "    2    " + "   3    ")
    print("   _______" + "_________" + "_______ ")
    print("  |       " + "|       |" + "       |")
    print("1 |   "+board[0][0]+"   " + "|   "+board[0][1]+"   |" + "   "+board[0][2]+"   |")
    print("  |_______" + "|_______|" + "_______|")
    print("  |       " + "|       |" + "       |")
    print("2 |   "+board[1][0]+"   " + "|   "+board[1][1]+"   |" + "   "+board[1][2]+"   |")
    print("  |_______" + "|_______|" + "_______|")
    print("  |       " + "|       |" + "       |")
    print("3 |   "+board[2][0]+"   " + "|   "+board[2][1]+"   |" + "   "+board[2][2]+"   |")
    print("  |_______" + "|_______|" + "_______|")

valid_input = False
while valid_input == False:
    if valid_input == False:
        print("Please enter an integer value between 1 - 3!")
        coordinate_x =int(input("Enter the X corrdinate: "))
        valid_input = coordinate_x.isdigit()
        if valid_input == False:
            print(coordinate_x.isdigit())
            print("Enter ang integer! Between 1 and 3!")
        elif valid_input == True and coordinate_x >= 1 and coordinate_x <= 3:
            print("Correct value")
            break


coordinate_y =str(input("Please enter the Y coordinate: "))
coordinate_y.upper

update_board(1,1,1)
update_board(0,1,2)
print_board()
for count in range(1):
    #print(board[count])
    print (board[0])
    print (board[1])
    print (board[2])
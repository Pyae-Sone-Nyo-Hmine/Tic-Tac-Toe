"""field in rows"""
row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

def field():
    print(row1)
    print(row2)
    print(row3)

def interaction():
    print("Welcome to TIC-TAC-TOE")
    print("")
    tutorial = input("Do you need instruction to walk you through the game? (y,n): ")
    if tutorial == "n":
        print("")

        ready = input("Press Enter to Start")


    if tutorial == "y":
        print("This is the field")
        print("")
        field()
        print("")
        print("You can enter the coordinate of the value using (column,row) terminology")
        print("or (x,y) where the top left is 1,1")
        print("")
        print(["1,1", "2,1", "3,1"])
        print(["1,2", "2,2", "3,2"])
        print(["1,3", "2,3", "3,3"])
        print("")
        print("Example input: 2,2")
        print("")
        print([" ", " ", " "])
        print([" ", "X", " "])
        print([" ", " ", " "])
        print("")

        ready = input("Press Enter to Start")
    print("")

""" Game Loop """
def game_loop():
    run = True
    while run:
        field()
        game_x = True
        """Algorithm for X"""

        x = input("Where do you want to put X ? (x,y): ")

        try:
            xcoord = x.split(",")
            xrow = int(xcoord[0])
            xcol = int(xcoord[1])
        except:
            xcol = "The user inputted something wrong"
            xrow = "The user inputted something wrong"

        if xcol == 1 and row1[xrow - 1] == " ":
            row1[xrow - 1] = "X"
            game_x = False
        elif xcol == 2 and row2[xrow-1] == " ":
            row2[xrow - 1] = "X"
            game_x = False
        elif xcol == 3 and row3[xrow-1] == " ":
            row3[xrow - 1] = "X"
            game_x = False
        else:
            while game_x:
                print("Enter the right value!!")
                x = input("Where do you want to put X ? (x,y): ")
                try:
                    xcoord = x.split(",")
                    xrow = int(xcoord[0])
                    xcol = int(xcoord[1])
                except:
                    xcol = "The user inputted something wrong"
                    xrow = "The user inputted something wrong"

                if xcol == 1 and row1[xrow - 1] == " ":
                    row1[xrow - 1] = "X"
                    game_x = False
                elif xcol == 2 and row2[xrow - 1] == " ":
                    row2[xrow - 1] = "X"
                    game_x = False
                elif xcol == 3 and row3[xrow - 1] == " ":
                    row3[xrow - 1] = "X"
                    game_x = False


        if row1[0] == "X" and row1[1] == "X" and row1[2] == "X":
            field()
            print("X Won!!")
            break

        if row2[0] == "X" and row2[1] == "X" and row2[2] == "X":
            field()
            print("X Won!!")
            break

        if row3[0] == "X" and row3[1] == "X" and row3[2] == "X":
            field()
            print("X Won!!")
            break

        if row1[0] == "X" and row2[0] == "X" and row3[0] == "X":
            field()
            print("X Won!!")
            break

        if row1[1] == "X" and row2[1] == "X" and row3[1] == "X":
            field()
            print("X Won!!")
            break

        if row1[2] == "X" and row2[2] == "X" and row3[2] == "X":
            field()
            print("X Won!!")
            break

        if row1[0] == "X" and row2[1] == "X" and row3[2] == "X":
            field()
            print("X Won!!")
            break

        if row1[2] == "X" and row2[1] == "X" and row3[0] == "X":
            field()
            print("X Won!!")
            break

        if " " not in row1 and " " not in row2 and " " not in row3:
            print("It's a tie!!")
            break
        """Algorithm for O"""

        field()
        game_o = True

        o = input("Where do you want to put O ? (x,y): ")
        try:
            ocoord = o.split(",")
            orow = int(ocoord[0])
            ocol = int(ocoord[1])
        except:
            orow = "The user entered the wrong value"
            ocol = "The user entered the wrong value"
        if ocol == 1 and row1[orow - 1] == " ":
            row1[orow - 1] = "O"
            game_o = False
        elif ocol == 2 and row2[orow - 1] == " ":
            row2[orow - 1] = "O"
            game_o = False
        elif ocol == 3 and row3[orow - 1] == " ":
            row3[orow - 1] = "O"
            game_o = False
        else:
            while game_o:
                print("Enter the right value!!")
                o = input("Where do you want to put 0 ? (x,y): ")
                try:
                    ocoord = o.split(",")
                    orow = int(ocoord[0])
                    ocol = int(ocoord[1])
                except:
                    orow = "The user entered the wrong value"
                    ocol = "The user entered the wrong value"

                if ocol == 1 and row1[orow - 1] == " ":
                    row1[orow - 1] = "O"
                    game_o = False
                elif ocol == 2 and row2[orow - 1] == " ":
                    row2[orow - 1] = "O"
                    game_o = False
                elif ocol == 3 and row3[orow - 1] == " ":
                    row3[orow - 1] = "O"
                    game_o = False

        if row1[0] == "O" and row1[1] == "O" and row1[2] == "O":
            field()
            print("0 Won!!")
            break

        if row2[0] == "O" and row2[1] == "O" and row2[2] == "O":
            field()
            print("O Won!!")
            break

        if row3[0] == "O" and row3[1] == "O" and row3[2] == "O":
            field()
            print("O Won!!")
            break

        if row1[0] == "O" and row2[0] == "O" and row3[0] == "O":
            field()
            print("O Won!!")
            break

        if row1[1] == "O" and row2[1] == "O" and row3[1] == "O":
            field()
            print("O Won!!")
            break

        if row1[2] == "O" and row2[2] == "O" and row3[2] == "O":
            field()
            print("O Won!!")
            break

        if row1[0] == "O" and row2[1] == "O" and row3[2] == "O":
            field()
            print("O Won!!")
            break

        if row1[2] == "O" and row2[1] == "O" and row3[0] == "O":
            field()
            print("O Won!!")
            break

        if " " not in row1 and " " not in row2 and " " not in row3:
            print("It's a tie!!")
            break

# runs program in console
interaction()
game_loop()
play = input("Do you want to play again? (y or n): ")
while play == "y":
    row1 = [" ", " ", " "]
    row2 = [" ", " ", " "]
    row3 = [" ", " ", " "]
    game_loop()
    play = input("Do you want to play again? (y or n): ")
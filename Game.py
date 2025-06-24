# Imports
import os
import time
import msvcrt

# Clear function
def Clear():
    os.system("cls" if os.name == "nt" else "clear")

# Input function
def GetInput():
    if msvcrt.kbhit():
        Key = msvcrt.getch().decode("utf-8")
        return Key
    else: 
        return None
    
# Grid setup
Rows = 5
Columns = 10
Grid = [[" " for _ in range(Columns)] for _ in range(Rows)]

# Sprite creation
Player_x = Columns // 2
Player_y = Rows // 2
Grid[Player_y][Player_x] = "P"


# Game Loop
while True:

    # Clear
    Clear()

    Grid = [[" " for _ in range(Columns)] for _ in range(Rows)]
    Grid[Player_y][Player_x] = "P"

    # Print grid
    for Row in Grid:
        print("|" +"".join(Row) + "|")
    
    # Get key input
    Key = GetInput()
    if Key == "a" and Player_x > 0:
        Player_x -= 1
    elif Key == "d" and Player_x < Columns - 1:
        Player_x += 1

    time.sleep(0)
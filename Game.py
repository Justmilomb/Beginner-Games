# Imports
import os
import time
import msvcrt
import random

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
Rows = 20
Columns = 10
Grid = [[" " for _ in range(Columns)] for _ in range(Rows)]

# Sprite creation
Player_x = Columns // 2
Player_y = Rows // 2
Grid[Player_y][Player_x] = "P"
Enemies = []


# Game Loop
while True:

    # Clear
    Clear()
    time.sleep(0.005)

    # Print grid
    for Row in Grid:
        print("|" +"".join(Row) + "|")
    
    # Get key input
    Key = GetInput()
    if Key == "a" and Player_x > 0:
        Player_x -= 1
    elif Key == "d" and Player_x < Columns - 1:
        Player_x += 1
    elif Key == "w" and Player_y > 0:
        Player_y -= 1
    elif Key == "s" and Player_y < Rows -1:
        Player_y += 1

    Grid = [[" " for _ in range(Columns)] for _ in range(Rows)]
    Grid[Player_y][Player_x] = "P"
    if random.random() < 0.02:
        NewEnemy = {"x": random.randint(0, Columns - 1), "y": 0 }
        Enemies.append(NewEnemy)

    for Enemy in Enemies:
        if Enemy["x"] == Player_x and Enemy["y"] == Player_y:
            print("Game over!")
            exit()

    
    for Enemy in Enemies:
        Enemy["y"] += 1
        
    for Enemy in Enemies:
        Grid[Enemy["y"]][Enemy["x"]] = "X"

    Enemies = [Enemy for Enemy in Enemies if Enemy["y"] < Rows]

    for Enemy in Enemies:
        Enemy["y"] += 1
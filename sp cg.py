import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
current_x, current_y = initial_tx, initial_ty

while True:
    remaining_turns = int(input())   
    move_string = ""
    if current_y<light_y:
        move_string = "S"
        current_y = current_y + 1
    elif current_y>light_y:
        move_string = "N"
        current_y = current_y - 1
    if current_x<light_x:
        move_string = move_string + "E"
        current_x = current_x + 1
    elif current_x>light_x:
        move_string = move_string + "W"
        current_x = current_x - 1
   
    print(move_string)

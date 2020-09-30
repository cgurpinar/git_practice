def is_integer(n):
    try:
        int(n)
    except ValueError:
        pass
    else:
        return int(n)


tic_tac = {3 - i : { 1 : " ", 2 : " ", 3 : " "} for i in range(3)}
w_dict = {"winner": "", "count": 0}
numbers = [1, 2, 3]
is_it_win_or_draw = False
is_user_moved = False
count = 0
users_input = []

print("---------")
for i in range(3,0,-1):
    print(f"| {tic_tac[i][1]} {tic_tac[i][2]} {tic_tac[i][3]} |")
print("---------")

while not is_it_win_or_draw:
    u_coor_input = input("Enter the coordinates: ")
    u_coor = [x for x in u_coor_input.split()]
       
    if len(u_coor) == 2 and is_integer(u_coor[0]) and is_integer(u_coor[1]):
        coor_x = int(u_coor[0])
        coor_y = int(u_coor[1])
    
        if coor_x in numbers and coor_y in numbers:
            if tic_tac[coor_y][coor_x] != "X" and tic_tac[coor_y][coor_x] != "O":
                users_input.append(u_coor_input)
                if count % 2 == 0:
                    count += 1
                    tic_tac[coor_y][coor_x] = "X"
                    print("---------")
                    for i in range(3,0,-1):
                        print(f"| {tic_tac[i][1]} {tic_tac[i][2]} {tic_tac[i][3]} |")
                    print("---------")
                    is_user_moved = True
                else:
                    count += 1
                    tic_tac[coor_y][coor_x] = "O"
                    print("---------")
                    for i in range(3,0,-1):
                        print(f"| {tic_tac[i][1]} {tic_tac[i][2]} {tic_tac[i][3]} |")
                    print("---------")
                    is_user_moved = True
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")
    
    if is_user_moved:
        for i in range(3,0,-1):
            if tic_tac[i][1]==tic_tac[i][2]==tic_tac[i][3]=="X" or tic_tac[i][1]==tic_tac[i][2]==tic_tac[i][3]=="O":
                w_dict["winner"] = tic_tac[i][1]
                w_dict["count"] += 1 
            elif tic_tac[3][i]==tic_tac[2][i]==tic_tac[1][i]=="X" or tic_tac[3][i]==tic_tac[2][i]==tic_tac[1][i]=="O":
                w_dict["winner"] = tic_tac[3][i]
                w_dict["count"] += 1
                       
        if tic_tac[3][1]==tic_tac[2][2]==tic_tac[1][3]=="X" or tic_tac[3][1]==tic_tac[2][2]==tic_tac[1][3]=="O":
            w_dict["winner"] = tic_tac[3][1]
            w_dict["count"] += 1
        elif tic_tac[1][1]==tic_tac[2][2]==tic_tac[3][3]=="X" or tic_tac[1][1]==tic_tac[2][2]==tic_tac[3][3]=="O":
            w_dict["winner"] = tic_tac[1][1]
            w_dict["count"] += 1

        if w_dict["count"] >= 2:
            is_it_win_or_draw = True
            print("Impossible")
        elif w_dict["count"] == 1:
            is_it_win_or_draw = True
            print("{} wins".format(w_dict["winner"]))
        elif not w_dict["count"] and len(users_input) == 9:            
            is_it_win_or_draw = True
            print("Draw")
        else:
            print("Game not finished")



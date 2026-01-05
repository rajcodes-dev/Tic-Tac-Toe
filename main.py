moves = ['','','',
         '','','',
         '','','']

variable = f"{moves[0]}  | {moves[1]}  | {moves[2]} \n\
_ | _ | _ \n\
{moves[3]}  | {moves[4]}  | {moves[5]} \n\
_ | _ | _ \n\
{moves[6]}  | {moves[7]}  | {moves[8]} \n"

print(variable)

count = 0

while True:
    player_1 = input("Enter the move (player-1): ")
    p = int(input("Enter the position of player - 1(1 to 9): "))
    player_2 = input("Enter the move (player-2): ")
    p2 = int(input("Enter the position of player - 2(1 to 9): "))

    moves[p-1] = player_1
    moves[p2-1] = player_2

    variable = f"{moves[0]}  | {moves[1]}  | {moves[2]} \n\
    _ | _ | _ \n\
    {moves[3]} | {moves[4]} | {moves[5]} \n\
    _ | _ | _ \n\
    {moves[6]} | {moves[7]} | {moves[8]}\n"

    print(variable)
    count += 1
    print(count)
    if count == 5:
        break
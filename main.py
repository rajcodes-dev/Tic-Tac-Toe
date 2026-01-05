moves = ['','','',
         '','','',
         '','','']

already = []

variable = f"1 | 2 | 3 \n\
_ | _ | _ \n\
4 | 5 | 6 \n\
_ | _ | _ \n\
7 | 8 | 9 \n"

print(variable)

player_1 = 'X'
player_2 = 'O'
count = 0

while True:
    p = int(input("Enter the position of player - 1(1 to 9): "))
    p2 = int(input("Enter the position of player - 2(1 to 9): "))

    if p in already:
        continue
    if p2 in already:
        continue

    already.append(p)
    already.append(p2)

    moves[p-1] = player_1
    moves[p2-1] = player_2

    variable = f"{moves[0]}  | {moves[1]}  | {moves[2]} \n\
    _ | _ | _ \n\
    {moves[3]} | {moves[4]} | {moves[5]} \n\
    _ | _ | _ \n\
    {moves[6]} | {moves[7]} | {moves[8]}\n"

    if (moves[0] and moves[1] and moves[2]) == 'X' or\
        (moves[3] and moves[4] and moves[5]) == 'X' or\
        (moves[6] and moves[7] and moves[8]) == 'X':
        print(variable)
        print("You won! 1")
        break

    if (moves[0] and moves[1] and moves[2]) == 'O' or\
        (moves[3] and moves[4] and moves[5]) == 'O' or\
        (moves[6] and moves[7] and moves[8]) == 'O':
        print(variable)
        print("You won! 2")
        break

    if (moves[0] and moves[3] and moves[6]) == 'O' or\
        (moves[1] and moves[4] and moves[7]) == 'O' or\
        (moves[2] and moves[5] and moves[8]) == 'O':
        print(variable)
        print("You won! 3")
        break

    if (moves[0] and moves[3] and moves[6]) == 'X' or\
        (moves[1] and moves[4] and moves[7]) == 'X' or\
        (moves[2] and moves[5] and moves[8]) == 'X':
        print(variable)
        print("You won! 4")
        break

    if (moves[0] and moves[4] and moves[8]) == 'X' or\
        (moves[2] and moves[4] and moves[6]) == 'X' or\
        (moves[0] and moves[4] and moves[8]) == 'O' or\
        (moves[2] and moves[4] and moves[6]) == 'O':
        print(variable)
        print("You won! 5")
        break

    print(variable)
    count += 1
    print(count)
    if count == 5:
        break
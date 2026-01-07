class GameController():

    def __init__(self, user_interface):
        self.user_interface = user_interface

    def run(self):
        while True:
            moves = ['','','',
                    '','','',
                    '','','']

            already = []

            variable = f"""
             {1} | {2} | {3}
            ---+---+---
             {4} | {5} | {6} 
            ---+---+---
             {7} | {8} | {9}
            """

            print(variable)
            player_1 = 'X'
            player_2 = 'O'
            while True:
                while True:
                    while True:
                        try:
                            p = self.user_interface.user_position()
                            break
                        except:
                            print("it only except integers.")

                    if p in already:
                        print("Don't enter the position again!")
                        continue
                    else:
                        break

                already.append(p)

                moves[p-1] = player_1

                variable = f"""
                {moves[0]} | {moves[1]} | {moves[2]}
                ---+---+---
                {moves[3]} | {moves[4]} | {moves[5]} 
                ---+---+---
                {moves[6]} | {moves[7]} | {moves[8]}
                """

                if moves[0] == 'X' and moves[1] == 'X' and moves[2] == 'X' or\
                    moves[3] == 'X' and moves[4] == 'X' and moves[5] == 'X' or\
                    moves[6] == 'X' and moves[7] == 'X' and moves[8] == 'X':
                    print(variable)
                    print("Player-1 won!")
                    break

                if moves[0] == 'X' and moves[3] == 'X' and moves[6] == 'X' or\
                    moves[1] == 'X' and moves[4] == 'X' and moves[7] == 'X' or\
                    moves[2] == 'X' and moves[5] == 'X' and moves[8] == 'X':
                    print(variable)
                    print("Player-1 won!")
                    break

                if (moves[0] == 'X' and moves[4] == 'X' and moves[8] == 'X') or\
                    (moves[2] == 'X' and moves[4] == 'X' and moves[6] == 'X'):
                    print(variable)
                    print("Player-1 won!")
                    break

                if len(already) == 9:
                    print("Draw!!")
                    break

                print(variable)
                while True:
                    while True:
                        try:
                            p2 = int(input("Enter the position of player - 2(1 to 9): "))
                            break
                        except:
                            print("it only except integers.")

                    if p2 in already:
                        print("Don't enter the position again!")
                        continue
                    else:
                        break

                already.append(p2)
                moves[p2-1] = player_2

                variable = f"""
                {moves[0]} | {moves[1]} | {moves[2]}
                ---+---+---
                {moves[3]} | {moves[4]} | {moves[5]} 
                ---+---+---
                {moves[6]} | {moves[7]} | {moves[8]}
                """

                if moves[0] == 'O' and moves[1] == 'O' and moves[2] == 'O' or\
                    moves[3] == 'O' and moves[4] == 'O' and moves[5] == 'O' or\
                    moves[6] == 'O' and moves[7] == 'O' and moves[8] == 'O':
                    print(variable)
                    print("Player-2 won!")
                    break

                if moves[0] == 'O' and moves[3] == 'O' and moves[6] == 'O' or\
                    moves[1] == 'O' and moves[4] == 'O' and moves[7] == 'O' or\
                    moves[2] == 'O' and moves[5] == 'O' and moves[8] == 'O':
                    print(variable)
                    print("Player-2 won!")
                    break

                if (moves[0] == 'O' and moves[4] == 'O' and moves[8] == 'O') or\
                    (moves[2] == 'O' and moves[4] == 'O' and moves[6] == 'O'):
                    print(variable)
                    print("Player-2 won!")

                print(variable)
        
            if self.user_interface.play() == 'n':
                break

class UserInterface:

    def user_position(self):
        return int(input("Enter the position of player - 1(1 to 9): "))

    def play(self): 
        return input("Do you want to play again(y/n)?: ").lower().strip()

if __name__ == '__main__':
    user_interface = UserInterface()
    game_controller = GameController(user_interface)
    game_controller.run()
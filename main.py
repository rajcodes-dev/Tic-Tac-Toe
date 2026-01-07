class GameController():

    def __init__(self, user_interface):
        self.user_interface = user_interface

    def run(self):
        while True:
            moves = ['','','',
                    '','','',
                    '','','']

            already = []

            current_player = 'X'

            variable = f"""
             {1} | {2} | {3}
            ---+---+---
             {4} | {5} | {6} 
            ---+---+---
             {7} | {8} | {9}
            """

            print(variable)
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

                moves[p-1] = current_player

                variable = f"""
                {moves[0]} | {moves[1]} | {moves[2]}
                ---+---+---
                {moves[3]} | {moves[4]} | {moves[5]} 
                ---+---+---
                {moves[6]} | {moves[7]} | {moves[8]}
                """

                if moves[0] == current_player and moves[1] == current_player and moves[2] == current_player or\
                    moves[3] == current_player and moves[4] == current_player and moves[5] == current_player or\
                    moves[6] == current_player and moves[7] == current_player and moves[8] == current_player:
                    print(variable)
                    print(f"{current_player} won!")
                    break

                if moves[0] == current_player and moves[3] == current_player and moves[6] == current_player or\
                    moves[1] == current_player and moves[4] == current_player and moves[7] == current_player or\
                    moves[2] == current_player and moves[5] == current_player and moves[8] == current_player:
                    print(variable)
                    print(f"{current_player} won!")
                    break

                if (moves[0] == current_player and moves[4] == current_player and moves[8] == current_player) or\
                    (moves[2] == current_player and moves[4] == current_player and moves[6] == current_player):
                    print(variable)
                    print(f"{current_player} won!")
                    break

                if len(already) == 9:
                    print("Draw!!")
                    break

                print(variable)
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'

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
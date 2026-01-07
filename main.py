import os

class GameController():

    def __init__(self, user_interface):
        self.user_interface = user_interface

    def run(self):
        while True:
            moves = [' ',' ',' ',
                    ' ',' ',' ',
                    ' ',' ',' ']

            already = []

            current_player = 'X'

            winning_combos = [(0,1,2),(3,4,5),(6,7,8),
                              (0,3,6),(1,4,7),(2,5,8),
                              (0,4,8),(2,4,6)]

            variable = f"""
             {1} | {2} | {3}
            ---+---+---
             {4} | {5} | {6} 
            ---+---+---
             {7} | {8} | {9}
            """
            self.user_interface.clear_screen()
            print(variable)
            
            while True:
                p = self.user_interface.get_valid_moves(already)

                already.append(p)

                moves[p-1] = current_player

                variable = f"""
                 {moves[0]} | {moves[1]} | {moves[2]}
                ---+---+---
                 {moves[3]} | {moves[4]} | {moves[5]} 
                ---+---+---
                 {moves[6]} | {moves[7]} | {moves[8]}
                """
                won = False
                for a,b,c in winning_combos:
                    if moves[a] == current_player and moves[b] == current_player and moves[c] == current_player:
                        print(variable)
                        print(f"{current_player} won!")
                        won = True
                        break
                if won == True:
                    break

                if len(already) == 9:
                    print("Draw!!")
                    break

                print(variable)
                if current_player == 'X':
                    current_player = 'O'
                else:
                    current_player = 'X'
            if  self.user_interface.play() == 'n':
                break

class UserInterface:

    def clear_screen(self):
        os.system('cls')

    def get_valid_moves(self, already):
        while True:
            while True:
                try:
                    p = self.user_position()
                    if p < 1 or p > 9:
                        print("Invalid input! Please choose 1-9.")
                        continue
                    break
                except:
                    print("it only except integers.")

            if p in already:
                print("Don't enter the position again!")
                continue
            else:
                return p

    def user_position(self):
        return int(input("Enter the position(1 to 9): "))

    def play(self): 
        return input("Do you want to play again(y/n)?: ").lower().strip()

if __name__ == '__main__':
    user_interface = UserInterface()
    game_controller = GameController(user_interface)
    game_controller.run()
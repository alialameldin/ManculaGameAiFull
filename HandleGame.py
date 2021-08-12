from time import time
from numpy import  inf
negative_infinity = -inf
postitive_infinity = inf
from time import sleep
class Handle_Game():


    def start_game(self,game,player1,player2):
        current_player= player1
        other_player= player2
        print("Game started....")
        while not (game.isterminal()):
            while not game.isterminal():
                current_player.turn()
                if current_player.type :
                    print("") #new line
                    t1=time()
                _,move = current_player.make_move(game)
                t = game.player_move(current_player.type, move)
                if (current_player.type):
                    print("Hole {}  choosed".format(move))
                    print("Number of total cutoff {}".format(current_player.cutoff))
                    print("total leafs :{} ".format(current_player.leaf_nodes))
                    current_player.cutoff =0
                    current_player.leaf_nodes = 0

                game.print_board()
                if not t:
                    break
                sleep(.5)
            if current_player.type:
                t2 = time()
                print("Time consumed = {} sec ".format(round(t2-t1),5))
            temp = current_player
            current_player = other_player
            other_player = temp
        print()
        print('GAME OVER')
        game.print_board()
        game.who_won()



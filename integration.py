from Game import MancalaGame
from HandleGame import  Handle_Game
import  player

if __name__ == "__main__":

        stealing=input("For Playing with stealing press s without stealing press w ")
        while not (stealing =='w' or stealing =='s'):
            stealing = input("Not valid :For Playing with stealing press s without stealing press w ")
        if stealing =='t':
            stealing =True
        elif stealing == 'w':
            stealing =False

        ### choose level of Game
        level = str(input("Choose game level 1 for medium 2 for hard  : \n ").replace(" ", ""))
        while True:
            if len(level) == 0 or not level.isnumeric() or level.isalpha()  or any ( c in level for c in ".!@#$%^&*()-+?_=,<>\""):
                level = str(input("Choose game level 1 for medium 2 for hard  : \n ").replace(" ", ""))
            elif not (int(level)== 1 or int(level)== 2):
                level = str(input("Choose game level 1 for medium 2 for hard  : \n ").replace(" ", ""))
            else:
                level = int(level)
                print( f"You choosed Level {level}")
                break

        game = MancalaGame(level=level,stealing=stealing)
        game.print_board()
        handle_game  = Handle_Game()
        who_first = input("Who Playes first? if you press y if Ai press a \n")
        while not (who_first == 'a' or who_first == 'y'):
            print("Not Valid ")
            who_first = input("Who Playes first? if you press y if Ai press a \n")
        if who_first =='y':
            p1 = player.HumanPlayer(1)
            p2 = player.AI_Player(2,level)
            handle_game.start_game(game, p1, p2)
        if who_first =='a':
            p1 = player.AI_Player(1,level)
            p2 = player.HumanPlayer(2)
            handle_game.start_game(game, p1, p2)
        print()
        print()



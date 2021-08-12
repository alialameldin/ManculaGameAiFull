import sys
sys.setrecursionlimit(10000)
from numpy import  inf
negative_infinity = -inf
postitive_infinity = inf



class MancalaGame():
    def __init__(self ,level, board = None, stealing = True):
        self.stealing = stealing
        self.level=level
        if board!=None: # you want to start at certain board state
            self.board = board
        else:
            self.board=[4,4,4,4,4,4,0,4,4,4,4,4,4,0] # initial state



    def player_move(self,player,hole): #player = True or False

        playagain = False

        stones = self.board[hole]
        round = hole+1
        self.board[hole]=0
        # handle the other mancala for each player
        while stones > 0:
            if (player) and round == 6:       #player two  ==> 0-5
                round == 7
            if (not player) and round == 13:  #player one  ==> 0-5
                round = 0

            # round robin on the holes to add a stone
            self.board[round] = self.board[round]+1
            stones -=1

            if stones == 0:
                lasthole = round
            else: ## holes from 0 to 13
                round = round +1
                if round > 13 :
                    round = 0

        # handle turns
        if (not player) and round == 6 :
             playagain = True  # False

        elif player and round == 13:
            playagain = True # True

        # stealing  or not
        elif (not player) and self.stealing and self.board[lasthole] == 1 and lasthole < 6 :
            if self.board[12-lasthole] != 0:
                self.board[6] = self.board[6] +  self.board[lasthole] + self.board[12-lasthole]
                self.board[lasthole] = 0
                self.board[12-lasthole]=0


        elif player and self.stealing and self.board[lasthole] == 1 and lasthole > 6  :
            if self.board[12-lasthole] != 0:
                self.board[13] = self.board[13] +  self.board[lasthole] + self.board[12-lasthole]
                self.board[lasthole] = 0
                self.board[12-lasthole]=0

        return  playagain

    def possible_moves(self):
        possible_moves = 0
        for i, a in enumerate(self.board[7:13]):
            if a > 0:
                possible_moves+=1
        return  possible_moves



    def isterminal(self):
        player1side = 0
        player2side = 0
        for hole in range(6):
            player1side = player1side + self.board[hole]
            player2side = player2side + self.board[hole + 7]
        if (player1side == 0 or player2side == 0):
            self.board[6] = self.board[6] + player1side
            self.board[13] = self.board[13] + player2side
            for hole in range(6):
                self.board[hole] = 0
                self.board[12-hole] = 0
            return True
        return False



    def who_won(self):
        # who won
        if ( self.board[6] >  self.board[13]):
            print("You won") #player 1
        elif ( self.board[6] <  self.board[13]):
            print("AI won") # player2
        else:
            print("No one Win it is Draw ")


    def static_eval(self):
        if self.level == 2:
            if self.isterminal():
                if self.board[13] > self.board[6]:
                    return 100
                elif self.board[13] == self.board[6]:
                    return 0
                else:
                    return -100
            else:
                score1 = self.another_turn_opportunities() * 0.1
                score2 = (self.board[13] - self.board[6]) * .45
                score3 = self.stealing_opportunities_for_opponent() * (-0.1)
                score4 = self.stealing_opportunities() * .05
                return score1+score2+score3+score4
        elif self.level == 1:
            if self.isterminal():
                if self.board[13] > self.board[6]:
                    return 100
                elif self.board[13] == self.board[6]:
                    return 0
                else:
                    return -100
            else:
                score2 = (self.board[13] - self.board[6]) * .45
                return score2
        else :
            pass
            ## will not happen



    def check(self):
        mancala1 = self.board[13]
        mancala2 = self.board[6]
        if mancala1 > 24:
            return 25
        elif mancala2 > 24:
            return -25
        else:
            return 0



    ## not used yet
    def another_turn_opportunities_for_opponenet(self):
        count=0.0
        for i,a in enumerate(self.board[0:6]):
            if i+a == 6 :
                count +=1
        return float(count)



    def another_turn_opportunities(self):
        count=0.0
        for i,a in enumerate(self.board[7:13]):
            if (7+i)+a == 13 or (a%13)+(i+7)-13 ==1 :
                count +=1
        return float(count)
    
    def stealing_opportunities(self):
        count = 0
        if not self.stealing:
            return 0.0
        else:
            emptyholes=0
            list_of_empty=[]
            for i, a in enumerate(self.board[7:13],7):
                if a == 0:
                    emptyholes +=1
                    list_of_empty.append(int(i+a))
            if emptyholes == 0:
                return 0
            else:
                for i, a in enumerate(self.board[7:13],7):
                    if  a +i in list_of_empty and  not a ==0:
                        count+=1
                return count

    def stealing_opportunities_for_opponent(self):
        count = 0
        if not self.stealing:
            return 0.0
        else:
            emptyholes = 0
            list_of_empty = []
            for i, a in enumerate(self.board[0:6]):
                if a == 0:
                    emptyholes += 1
                    list_of_empty.append(int(i + a))
            if emptyholes == 0:
                return 0
            else:
                for i, a in enumerate(self.board[0:6]):
                    if a + i in list_of_empty and not a == 0:
                        count += 1
                return count

    def print_board(self):
        i = 0
        for i in range(len(self.board)):
            if (self.board[i]) < 10 :
                self.board[i]=" "+str(self.board[i])
            else:
                self.board[i]=str(self.board[i])
        print()
        print("            |12|  |11|  |10|   |9|    |8|   |7| ")
        print("+---------+-----+------+-----+------+-----+-----+---------+")
        print("|Opponent | " + str(self.board[12]) + "  | " + (self.board[11])
              + "   | " + (self.board[10]) + "  | " + (self.board[9])
              + "   | " + (self.board[8]) + "  | " + (self.board[7]) + "  |    You  |")
        print("| " + (self.board[13]) + "      |----+----+----+----+----+----+-------| " + (self.board[6]) + "      |")
        print("|         | " + (self.board[0]) + "  | " + (self.board[1])
              + "   | " + (self.board[2]) + "  | " + (self.board[3])
              + "   | " + (self.board[4]) + "  | " + (self.board[5]) + "  |         |")
        print("+---------+-----+------+-----+------+-----+-----+---------+")
        print("            |0|   |1|    |2|    |3|   |4|   |5|            ")
        for i in range(len(self.board)):
            self.board[i]=int(self.board[i])

    def validate_move(self,move):
        if not (0 <= move  <= 5 ) :
            print("you must choose a hole in your side from 0 to 5 ")
            return False
        elif self.board[move] == 0: #empty hole
            print("You must choose a non-empty hole ")
            return False
        return True



import random
import copy
class ConnectFour:
    def __init__(self):
        self.player1= ""
        self.player2 = "P2"
        self.columncount = 7
        self.rowcount =6
        self.board = {
        6: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        5: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        4: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        3: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        2: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        1: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "}
        }
        self.played = {1: 0,2: 0,3:0,4: 0,5: 0,6: 0,7: 0} #stores how many values have been played in each row
        self.columnorder = [4,3,5,2,6,1,7] #Order in which the minmax algorithm goes through columns


    def print_board(self):
        output = ""
        for _,line in self.board.items():
            output += "----------------------\n"
            for _,value in line.items():
                output += "|" +str(value)
            output +="|\n"
        output += "----------------------"
        print(output)

    def play(self,column: int,player,board,played):
        """ Function that plays """
        if played[column] <6:
            row = played[column]+1
            board[row][column] = str(player)
            played[column] +=1
        return board

    def ask(self):
        """This is the main game loop that runs the game"""
        # Ask the player to pick a symbol that will be displayed on the screen
        self.player1 = str(input("Pick a symbol: "))[0] + " "
        while True:
            column = int(input("Pick a column (1-7): "))
            row = self.played[column]+1
            self.board = self.play(column, self.player1,self.board,self.played)
            win1 = self.check_win_cell(row,column,self.player1,self.board)
            self.print_board()
            if win1:
                print("Player win")
                return False
            minmax = self.minmax(self.columnorder,self.board,self.played,1,False)
            best_column = minmax[0]
            print(minmax)
            if best_column is None:
                print("No empty cells left")
                return False
            row2 = self.played[best_column]+1
            self.board = self.play(best_column,self.player2,self.board,self.played)
            win2 = self.check_win_cell(row2,best_column,self.player2,self.board)
            self.print_board()
            if win2:
                print("AI win")
                return False

    def is_valid_location(self,r,c):
        return c in range(1,self.columncount+1) and r in range(1,self.rowcount+1)

    def check_win_horizontal(self,r,c,p,board):
        score = 0
        i = 0
        while i >= 0:
            if self.is_valid_location(r,c+i):
                if board[r][c+i] == p:
                    score +=1
                    i += 1
                else:
                    break
            else:
                break
        i = -1
        while i < 0:
            if self.is_valid_location(r,c+i):
                if board[r][c+i] == p:
                    score += 1
                    i -= 1
                else:
                    break
            else:
                break
        return score >=4


    def check_win_vertical(self,r,c,p,board):
        score = 0
        i = 0
        while i <= 0:
            if self.is_valid_location(r+i,c):
                if board[r+i][c] == p:
                    score += 1
                    i -= 1
                else:
                    break
            else:
                break
        return score >=4

    def check_win_diagonal_down(self,r,c,p,board):
        score = 0
        i = 0
        while i >= 0:
            if self.is_valid_location(r-i,c+i):
                if board[r-i][c+i] == p:
                    score +=1
                    i += 1
                else:
                    break
            else:
                break
        i = -1
        while i < 0:
            if self.is_valid_location(r-i,c+i):
                if board[r-i][c+i] == p:
                    score += 1
                    i -= 1
                else:
                    break
            else:
                break
        return score >=4


    def check_win_diagonal_up(self,r,c,p,board):
        score = 0
        i = 0
        while i >= 0:
            if self.is_valid_location(r+i,c+i):
                if board[r+i][c+i] == p:
                    score +=1
                    i += 1
                else:
                    break
            else:
                break
        i = -1
        while i < 0:
            if self.is_valid_location(r+i,c+i):
                if board[r+i][c+i] == p:
                    score += 1
                    i -= 1
                else:
                    break
            else:
                break
        return score >=4

    def check_win_cell(self,r,c,p,board):
        """Checks a specific cell and whether or not it gives a victory"""
        score1 = self.check_win_diagonal_down(r,c,p,board)
        score2 = self.check_win_diagonal_up(r,c,p,board)
        score3 = self.check_win_horizontal(r,c,p,board)
        score4 = self.check_win_vertical(r,c,p,board)
        return score1 or score2 or score3 or score4

    def get_valid_columns(self,played,columnorder):
        for i in range(len(columnorder)-1,-1,-1):
            if played[columnorder[i]] >=self.rowcount:
                columnorder.pop(i)

    def minmax(self,columnorder,board,played,depth,maxplayer,alpha=-99999999,beta=9999999):
        newcolumnorder = copy.deepcopy(columnorder)
        self.get_valid_columns(played,newcolumnorder)
        if depth == 0:
            return None,0
        if len(newcolumnorder) == 0:
            return None,0
        column = 4
        if maxplayer: # Human player
            value = -99999999
            for c in newcolumnorder:
                newplayed = copy.deepcopy(played)
                newboard = copy.deepcopy(board)
                r = newplayed[c] +1
                self.play(c,self.player1,newboard,newplayed)
                if self.check_win_cell(r,c,self.player1,newboard):
                    #print("-"*(3 - depth), "Player win found!")
                    return c, 9999999
                #print("-"*(3 - depth), "Searching", c)
                new_value = self.minmax(newcolumnorder,newboard,newplayed,depth-1,False,alpha,beta)[1]
                if new_value > value:
                    value = new_value
                    column = c
                alpha = max(alpha,value)
                if alpha >= beta:
                    break
            #print("-"*(3 - depth), value, column)
            return column, value
        else: #minplayer, AI
            value = 9999999
            for c in newcolumnorder:
                newplayed = copy.deepcopy(played)
                newboard = copy.deepcopy(board)
                r = newplayed[c] +1
                self.play(c,self.player2,newboard,newplayed)

                if self.check_win_cell(r,c,self.player2,newboard):
                    #print(" "*(3 - depth), "AI win found")
                    return c, -9999999
                #print(" "*(3 - depth), "Searching", c)
                new_value = self.minmax(newcolumnorder,newboard,newplayed,depth-1,True,alpha,beta)[1]
                if new_value < value:
                    value = new_value
                    column = c
                beta = min(beta,value)
                if alpha >= beta:
                    break

            #print(" "*(3 - depth), value, column)
            return column, value

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
        """ Function that plays a player tag in a column"""
        if played[column] <6:
            row = played[column]+1
            board[row][column] = str(player)
            played[column] +=1
        return board

    def ask(self):
        """This is the main game loop that runs the game"""
        # Ask the player to pick a symbol that will be displayed on the screen
        self.print_board()
        self.player1 = str(input("Choose a symbol to use as a player tag: "))[0] + " "
        while True:
            column = int(input("Pick a column (1-7): "))
            row = self.played[column]+1
            self.board = self.play(column, self.player1,self.board,self.played)
            win1 = self.check_win_cell(row,column,self.player1,self.board)
            self.print_board()
            if win1:
                print("Player win")
                return False
            minmax = self.minmax(self.columnorder,self.board,self.played,8,False)
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
        """ r= row, c=column """
        return c in range(1,self.columncount+1) and r in range(1,self.rowcount+1)

    def check_win_horizontal(self,r,c,p,board):
        """ r= row, c=column, p=player"""
        score = 0
        emptyorp = 0 # Empty or player
        winrow = 0 #counts how many player tags are in a continous row
        i = 1
        while i <= 3:
            if self.is_valid_location(r,c+i):
                if board[r][c+i] == p:
                    score +=1
                    emptyorp +=1
                    i += 1
                    if score == emptyorp: #If emptyorp is larger than score, there must have been an empty cell in between, therefore it's not a contious row
                        winrow += 1
                elif board[r][c+i] == "  ":
                    emptyorp += 1
                    i +=1
                else: # Stops if the cell has the opposite players tag
                    break
            else:
                break
        i = -1
        continousrow = True
        while i >= -3:
            if self.is_valid_location(r,c+i):
                if board[r][c+i] == p:
                    emptyorp += 1
                    score += 1
                    i -= 1
                    if continousrow:
                        winrow += 1
                elif board[r][c+i] == "  ":
                    emptyorp +=1
                    continousrow = False
                    i -= 1
                else:
                    break
            else:
                break
        if emptyorp <3: #There is not enough space for a win
            score = 0
        return winrow, score, emptyorp


    def check_win_vertical(self,r,c,p,board):
        """ r= row, c=column, p=player"""
        score = 0
        i = -1
        while i >= -3:
            if self.is_valid_location(r+i,c):
                if board[r+i][c] == p:
                    score += 1
                    i -= 1
                else:
                    break
            else:
                break
        i = 1
        emptyorp = score #Empty or player
        while emptyorp <=3:
            if self.is_valid_location(r+i,c): # We already know any cell above must be empty so there is no reason to check that out
                emptyorp += 1
                i += 1
            else:
                break
        return score, score, emptyorp

    def check_win_diagonal_down(self,r,c,p,board):
        """ r= row, c=column, p=player"""
        score = 0
        i = 1
        emptyorp = 0 # empty or player
        winrow = 0
        while i <= 3:
            if self.is_valid_location(r-i,c+i):
                if board[r-i][c+i] == p:
                    score +=1
                    i += 1
                    if winrow == emptyorp:
                        winrow +=1
                    emptyorp += 1
                elif board[r-i][c+i]=="  ":
                    emptyorp +=1
                    i += 1
                else:
                    break
            else:
                break
        i = -1
        continousrow = True
        while i >= -3:
            if self.is_valid_location(r-i,c+i):
                if board[r-i][c+i] == p:
                    score += 1
                    i -= 1
                    emptyorp += 1
                    if continousrow:
                        winrow +=1
                elif board[r-i][c+i] == "  ":
                    continousrow = False
                    emptyorp += 1
                    i -= 1
                else:
                    break
            else:
                break
        return winrow, score, emptyorp


    def check_win_diagonal_up(self,r,c,p,board):
        """ r= row, c=column, p=player"""
        score = 0
        i = 1
        emptyorp = 0
        winrow = 0
        while i <= 3:
            if self.is_valid_location(r+i,c+i):
                if board[r+i][c+i] == p:
                    i += 1
                    score +=1
                    if emptyorp == winrow:
                        winrow += 1
                    emptyorp += 1
                elif board[r+i][c+i] == "  ":
                    i += 1
                    emptyorp += 1
                else:
                    break
            else:
                break
        i = -1
        continousrow = True
        while i < 0:
            if self.is_valid_location(r+i,c+i):
                if board[r+i][c+i] == p:
                    score += 1
                    i -= 1
                    emptyorp +=1
                    if continousrow:
                        winrow += 1
                elif board[r+i][c+i] == "  ":
                    continousrow = False
                    emptyorp += 1
                    i -= 1
                else:
                    break
            else:
                break
        return winrow, score, emptyorp

    def has_nearing_cells(self,r,c,board):
        if self.is_valid_location(r,c+1):
            if board[r][c+1] != "  ":
                return True
        if self.is_valid_location(r,c-1):
            if board[r][c-1] != "  ":
                return True
        if self.is_valid_location(r+1,c+1):
            if board[r+1][c+1] != "  ":
                return True
        if self.is_valid_location(r+1,c-1):
            if board[r+1][c-1] != "  ":
                return True
        return False


    def score_board(self,board,played):
        """ Counts potential scores around cells where someone has already played """
        board_score = 0
        c =1
        r = played[c]+1
        while c <= self.columncount:
            if r > self.rowcount:
                c +=1
                if c <= self.columncount:
                    r = played[c]+1
            else:
                board_score += self.check_score_cell(r,c,self.player1,board)
                board_score -= self.check_score_cell(r,c,self.player2,board)
                if self.has_nearing_cells(r,c,board):
                    r += 1
                else:
                    c +=1
                    if c <= self.columncount:
                        r = played[c]+1
        return board_score

    def give_points(self,winrow,score, emptyorp):
        if emptyorp <=2: #no more space for a win
            return 0
        if winrow >= 3: # 3 in a row
            return 15
        if score >= 3 or winrow ==2: # 2 in a continous row or 3 or more pieces within range for a winrow
            return 7
        if score >= 1: # At least 1 in range for a winrow
            return 4
        return 2 # no player tags in this row but enough space for a winrow
    def check_score_cell(self,r,c,p,board):
        """Returns a score for a cell depending on how many 1,2 and 3 in a rows there are"""
        winrow1, score1, emptyorp1 = self.check_win_diagonal_down(r,c,p,board)
        winrow2, score2, emptyorp2 = self.check_win_diagonal_up(r,c,p,board)
        winrow3, score3, emptyorp3 = self.check_win_horizontal(r,c,p,board)
        winrow4, score4, emptyorp4 = self.check_win_vertical(r,c,p,board)
        points1 = self.give_points(winrow1, score1, emptyorp1)
        points2 = self.give_points(winrow2, score2, emptyorp2)
        points3 = self.give_points(winrow3, score3, emptyorp3)
        points4 = self.give_points(winrow4, score4, emptyorp4)
        return points1 + points2 + points3 +points4
    def check_win_cell(self,r,c,p,board):
        """Checks a specific cell and whether or not it gives a victory"""
        score1 = self.check_win_diagonal_down(r,c,p,board)[0]
        score2 = self.check_win_diagonal_up(r,c,p,board)[0]
        score3 = self.check_win_horizontal(r,c,p,board)[0]
        score4 = self.check_win_vertical(r,c,p,board)[0]
        return score1 >= 3 or score2 >= 3 or score3 >= 3 or score4 >=3

    def get_valid_columns(self,played,columnorder):
        for i in range(len(columnorder)-1,-1,-1):
            if played[columnorder[i]] >=self.rowcount:
                columnorder.pop(i)

    def minmax(self,columnorder,board,played,depth,maxplayer,alpha=-99999999,beta=9999999):
        newcolumnorder = copy.deepcopy(columnorder)
        self.get_valid_columns(played,newcolumnorder)
        if depth == 0:
            return None,self.score_board(board,played)
        if len(newcolumnorder) == 0:
            return None,0
        column = newcolumnorder[0]
        if maxplayer: # Human player
            value = -99999999
            for c in newcolumnorder:
                newplayed = copy.deepcopy(played)
                newboard = copy.deepcopy(board)
                r = newplayed[c] +1
                self.play(c,self.player1,newboard,newplayed)
                if self.check_win_cell(r,c,self.player1,newboard):
                    return c, 1000000 + depth
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
                    return c, -1000000 -depth
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

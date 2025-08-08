import copy
import time

class ConnectFour:
    def __init__(self,rowcount=6,columncount=7):
        self.player1= ""
        self.player2 = "AI"
        self.columncount = columncount
        self.rowcount =rowcount
        self.board = [["  " for x in range(self.columncount +1)] for y in range(self.rowcount+1)]
        self.played = {1: 0,2: 0,3:0,4: 0,5: 0,6: 0,7: 0} #stores how many values have been played in each row
        self.columnorder = [4,3,5,2,6,1,7] #Order in which the minmax algorithm goes through columns
        self.columndepth = {1: 0,2: 0,3:0,4: 0,5: 0,6: 0,7: 0}
        self.memory= {}
    def print_board(self):
        output = ""
        for row in range(self.rowcount,0,-1):
            output += "----------------------\n"
            for column in range(1,self.columncount+1):
                value = self.board[row][column]
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

    def game_loop(self):
        """This is the main game loop that runs the game"""
        # Ask the player to pick a symbol that will be displayed on the screen
        self.print_board()
        self.player1 = str(input("Choose a symbol to use as a player tag: "))[0] + " "
        while True:
            column = int(input("Pick a column (1-7): "))
            row = self.played[column]+1
            self.play(column, self.player1,self.board,self.played)
            win1 = self.check_win_cell(row,column,self.player1,self.board)
            self.print_board()
            if win1:
                print("Player win")
                return False
            self.remove_column_if_full(column)
            if len(self.columnorder) == 0:
                print("Tie")
                return False
            minmax = self.iterative_deepening()
            best_column = minmax[0]
            print(minmax)
            row2 = self.played[best_column]+1
            self.play(best_column,self.player2,self.board,self.played)
            self.remove_column_if_full(best_column)
            if len(self.columnorder) ==0:
                print("Tie")
                return False
            self.columnorder = self.order_colummns(self.columnorder,self.columndepth)
            win2 = self.check_win_cell(row2,best_column,self.player2,self.board)
            self.print_board()
            if win2:
                print("AI win")
                return False

    def iterative_deepening(self):
        timeout = time.time() +5
        depth=1
        column,value = self.minmax(self.columnorder,self.board,self.played,depth,False)
        while True:
            print("Depth: "+str(depth))
            if abs(value) >= 1000000 or value == 0.5:
                return column, value
            depth += 1
            column,value = self.minmax(self.columnorder,self.board,self.played,depth,False)
            end_time = time.time()
            if timeout < end_time:
                return column, value

    def remove_column_if_full(self,column):
        if self.played[column] >= self.rowcount:
            self.columnorder.remove(column)
            return True
        return False

    def order_colummns(self,columnorder,columndepth): # Orders columns based on how deep the algorithm searches each of them
        return sorted(columnorder,key=lambda x: columndepth[x],reverse=True)

    def is_valid_location(self,r,c):
        """ r= row, c=column """
        return c in range(1,self.columncount+1) and r in range(1,self.rowcount+1)

    def check_win_horizontal(self,r,c,p,board):
        """ r= row, c=column, p=player"""
        return self.check_score_direction(r,c,p,0,1,board)


    def check_win_vertical(self,r,c,p,board):
        """ r= row, c=column, p=player"""
        return self.check_score_direction(r,c,p,1,0,board)

    def check_win_diagonal_down(self,r,c,p,board):
        """ r= row, c=column, p=player"""
        return self.check_score_direction(r,c,p,-1,1,board)


    def check_win_diagonal_up(self,r,c,p,board):
        """ r= row, c=column, p=player"""
        return self.check_score_direction(r,c,p,1,1,board)

    def check_score_direction(self,r,c,p,dr,dc,board):
        """ r= row, c=column, p=player"""
        score = 0
        i = 1
        emptyorp = 0
        winrow = 0
        while i <= 3:
            if self.is_valid_location(r+i*dr,c+i*dc):
                if board[r+i*dr][c+i*dc] == p:
                    i += 1
                    score +=1
                    if emptyorp == winrow:
                        winrow += 1
                    emptyorp += 1
                elif board[r+i*dr][c+i*dc] == "  ":
                    i += 1
                    emptyorp += 1
                else:
                    break
            else:
                break
        i = -1
        continousrow = True
        while i >= -3:
            if self.is_valid_location(r+i*dr,c+i*dc):
                if board[r+i*dr][c+i*dc] == p:
                    score += 1
                    i -= 1
                    emptyorp +=1
                    if continousrow:
                        winrow += 1
                elif board[r+i*dr][c+i*dc] == "  ":
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
        """ Counts scores around cells where someone has already played """
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
        if emptyorp <=2:

 #no more space for a win
            return 0
        if winrow >= 3: # 3 in a row
            return 10
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
        board_key = str(board)
        if board_key in self.memory:
            column = self.memory[board_key]
            newcolumnorder.remove(column)
            newcolumnorder.insert(0,column)
        if maxplayer:
            value = -99999999
        else:
            value = 99999999
        if depth == 0:
            return None,self.score_board(board,played)
        if len(newcolumnorder) == 0:
            return None,0.5
        column = newcolumnorder[0]
        if maxplayer: # Human player
            for c in newcolumnorder:
                newplayed = copy.deepcopy(played)
                newboard = copy.deepcopy(board)
                r = newplayed[c] +1
                self.play(c,self.player1,newboard,newplayed)
                if self.check_win_cell(r,c,self.player1,newboard):
                    self.columndepth[c] = depth
                    self.memory[board_key] = c
                    return c, 1000000 + depth
                new_value = self.minmax(newcolumnorder,newboard,newplayed,depth-1,False,alpha,beta)[1]
                if new_value > value:
                    value = new_value
                    column = c
                alpha = max(alpha,value)
                if alpha >= beta:
                    break
            self.columndepth[column] = depth
            self.memory[board_key] = column
            return column, value
        else: #minplayer, AI
            for c in newcolumnorder:
                newplayed = copy.deepcopy(played)
                newboard = copy.deepcopy(board)
                r = newplayed[c] +1
                self.play(c,self.player2,newboard,newplayed)
                if self.check_win_cell(r,c,self.player2,newboard):
                    self.columndepth[c] = depth
                    self.memory[board_key] = c
                    return c, -1000000 -depth
                new_value = self.minmax(newcolumnorder,newboard,newplayed,depth-1,True,alpha,beta)[1]
                if new_value < value:
                    value = new_value
                    column = c
                beta = min(beta,value)
                if alpha >= beta:
                    break
            self.columndepth[column] = depth
            self.memory[board_key] = column
            return column, value

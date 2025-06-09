import random
import copy
class ConnectFour:
    def __init__(self):
        self.player1= ""
        self.player2 = "P2"
        self.columncount = 6
        self.rowcount =7
        self.board = {
        6: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        5: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        4: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        3: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        2: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        1: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "}
        }
        self.played = {1: 0,2: 0,3:0,4: 0,5: 0,6: 0,7: 0}
        self.roworder = [4,3,5,2,6,1,7]
        self.board_tree = {}


    def print_board(self):
        output = ""
        for _,line in self.board.items():
            output += "----------------------\n"
            for _,value in line.items():
                output += "|" +str(value)
            output +="|\n"
        output += "----------------------"
        print(output)

    def play(self,row: int,player,board):
        if row > 7 or row < 1:
            print("Valitse numero väliltä 1 ja 7")
        if self.played[row] <6:
            column = self.played[row]+1
            board[column][row] = str(player)
            self.played[row] +=1
        self.print_board()

    def ask(self,player_name = None, pick_row = None):
        self.player1 = str(input("Pick a symbol: "))[0]+" " if not player_name else player_name[0]
        while True:
            row = int(input("Pick a row (1-7): ")) if not pick_row else pick_row
            column = self.played[row]+1
            self.play(row, self.player1,self.board)
            win1 = self.check_win_cell(column,row,self.player1,self.board)
            print(win1)
            if win1:
                return False
            row2 = random.randint(1,7)
            column2 = self.played[row2]+1
            self.play(row2,self.player2,self.board)
            win2 = self.check_win_cell(column2,row2,self.player2,self.board)
            print(win2)
            if win2:
                return False

    def check_cell(self,c,r,p):
        """c=coulumn, r= row, p=player"""
        if self.board[c][r] == p:
            return 1
        if self.board[c][r] == "  ":
            return 0
        return -1

    def is_valid_location(self,c,r):
        return c in range(1,self.columncount+1) and r in range(1,self.rowcount+1)

    def check_win_horizontal(self,c,r,p,board):
        score = 0
        i = 0
        while i >= 0:
            if self.is_valid_location(c,r+i):
                if board[c][r+i] == p:
                    score +=1
                    i += 1
                else:
                    i = -1
            else:
                i = -1
        while i < 0:
            if self.is_valid_location(c,r+i):
                if board[c][r+i] == p:
                    score += 1
                    i -= 1
                else:
                    i = 0
            else:
                i = 0
        return score >=4


    def check_win_vertical(self,c,r,p,board):
        score = 0
        i = 0
        while i <= 0:
            if self.is_valid_location(c+i,r):
                if board[c+i][r] == p:
                    score += 1
                    i -= 1
                else:
                    i = 9999
            else:
                i = 9999
        return score >=4

    def check_win_diagonal_down(self,c,r,p,board):
        score = 0
        i = 0
        while i >= 0:
            if self.is_valid_location(c-i,r+i):
                if board[c-i][r+i] == p:
                    score +=1
                    i += 1
                else:
                    i = -1
            else:
                i = -1
        while i < 0:
            if self.is_valid_location(c-i,r+i):
                if board[c-i][r+i] == p:
                    score += 1
                    i -= 1
                else:
                    i = 9999
            else:
                i = 9999
        return score >=4

    def check_win_diagonal_up(self,c,r,p,board):
        score = 0
        i = 0
        while i >= 0:
            if self.is_valid_location(c+i,r+i):
                if board[c+i][r+i] == p:
                    score +=1
                    i += 1
                else:
                    i = -1
            else:
                i = -1
        while i < 0:
            if self.is_valid_location(c+i,r+i):
                if board[c+i][r+i] == p:
                    score += 1
                    i -= 1
                else:
                    i = 0
            else:
                i = 0
            return score >=4
    def check_win_cell(self,c,r,p,board):
        score1 = self.check_win_diagonal_down(c,r,p,board)
        score2 = self.check_win_diagonal_up(c,r,p,board)
        score3 = self.check_win_horizontal(c,r,p,board)
        score4 = self.check_win_vertical(c,r,p,board)
        return score1 or score2 or score3 or score4

    def minmax(self,p,board,played):
        for r in range(1,8):
            newboard = copy.deepcopy(board)
            newplayed = copy.deepcopy(played)
            if played[r] >= self.columncount:
                pass
            else:
                c = played[r]+1
                self.play(r,p,newboard)
            c = played[r]
            if self.check_win_cell(c,r,p,newboard):
                pass
            else:
                if p == self.player1:
                    other_player = self.player2
                else:
                    other_player = self.player1
                self.minmax(other_player,newboard,newplayed)



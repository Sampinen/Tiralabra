import random

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

    def roworder(self):
        return [4,3,5,2,6,1,7]

    def print_board(self):
        output = ""
        for _,line in self.board.items():
            output += "----------------------\n"
            for _,value in line.items():
                output += "|" +str(value)
            output +="|\n"
        output += "----------------------"
        print(output)

    def play(self,row: int,player):
        if row > 7 or row < 1:
            print("Valitse numero väliltä 1 ja 7")
        if self.played[row] <6:
            column = self.played[row]+1
            self.board[column][row] = str(player)
            self.played[row] +=1
            self.weights[self.played[row]][row] = 0
            if column -1 in self.weights:
                self.weights[column-1][row] += 2

        self.print_board()
            

    def ask(self,player_name = None, pick_row = None):
        self.player1 = str(input("Pick a symbol: "))[0]+" " if not player_name else player_name[0]
        while True:
            row = int(input("Pick a row (1-7): ")) if not pick_row else pick_row
            self.play(row, self.player1)
            win1 = self.check_win(self.player1)
            if win1:
                return False
            self.check_scores(self.player2)
            win2 =self.check_win(self.player2)
            if win2:
                return False

    def check_cell(self,c,r,p):
        """c=coulumn, r= row, p=player"""
        if self.board[c][r] == p:
            return 1
        if self.board[c][r] == "  ":
            return 0
        return -10

    def is_valid_location(self,c,r):
        return c in range(1,self.columncount+1) and r in range(1,self.rowcount+1)

    def check_win_horizontal(self,c,r,p,board):
        score = 0
        i = 1
        while i > 0:
            if self.is_valid_location(c,r+i):
                if board[c][r+i] == p:
                    score +=1
                    i += 1
                else:
                    i = -1
            else:
                i = -1
        while i < 0:
            if self.is_valid_location(c,r-i):
                if board[c][r-i] == p:
                    score += 1
                    i -= 1
                else:
                    i = 0
            else:
                i = 0
        return score

    def check_win_vertical(self,c,r,p,board):
        score = 0
        i = -1
        while i < 0:
            if self.is_valid_location(c-i,r):
                if board[c-i][r] == p:
                    score += 1
                    i -= 1
                else:
                    i = 0
            else:
                i = 0
        return score
    
    def check_win_diagonal_down(self,c,r,p,board):
        score = 0
        i = 1
        while i > 0:
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
                    i = 0
            else:
                i = 0
            return score

    def check_win_diagonal_up(self,c,r,p,board):
        score = 0
        i = 1
        while i > 0:
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
            return score
    def check_win_cell(self,c,r,p,board):
        self.check_win_diagonal_down(c,r,p,board)
        self.check_win_diagonal_up(c,r,p,board)
        self.check_win_horizontal(c,r,p,board)
        self.check_win_vertical(c,r,p,board)

    def check_scores(self,player):
        score = -99999
        row = 0
        for r in range(1,8):
            if self.played[r] > 5:
                pass
            else:
                column = self.played[r]+1
                cell_score = self.check_score_cell(column,r,player)
                if cell_score > score:
                    row =r
                    score = cell_score
                if score ==3:
                    self.play(row,player)
                    return
        if row == 0:
            print("Kaikki ruudut täynnä")
        else:
            print(score,row)
            self.play(row,player)

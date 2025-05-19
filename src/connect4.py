import random

class ConnectFour:
    def __init__(self):
        self.player1= ""
        self.player2 = "P2"
        self.board = {
        6: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        5: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        4: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        3: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        2: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "},
        1: {1: "  ",2: "  ",3: "  ", 4: "  ", 5:"  ", 6:"  ",7:"  "}
        }
        self.weights = {
        6: {1: 1,2: 2,3: 3, 4: 4, 5: 3, 6: 2,7: 1},
        5: {1: 2,2: 3,3: 4, 4: 5, 5: 4, 6: 3,7: 2},
        4: {1: 3,2: 4,3: 5, 4: 6, 5: 5, 6: 4,7: 3},
        3: {1: 3,2: 4,3: 5, 4: 6, 5: 3, 6: 4,7: 3},
        2: {1: 2,2: 3,3: 4, 4: 5, 5: 4, 6: 3,7: 2},
        1: {1: 1,2: 2,3: 3, 4: 4, 5: 3, 6: 2,7: 1}
        }
        self.played = {1: 0,2: 0,3:0,4: 0,5: 0,6: 0,7: 0}

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
            self.board[self.played[row]+1][row] = str(player)
            self.played[row] +=1
        self.print_board()

    def ask(self):
        self.player1 = str(input("Pick a symbol: "))[0]+" "
        while True:
            row = int(input("Pick a row (1-7): "))
            self.play(row, self.player1)
            win1 = self.check_win(self.player1)
            if win1:
                return False
            self.play(random.randint(1,7),self.player2)
            win2 =self.check_win(self.player2)
            if win2:
                return False

    def check_cell(self,c,r,p):
        """c=coulumn, r= row, p=player"""
        if self.board[c][r] == p:
            return True
        return False


    def check_horizontal(self,c,r,p):
        """c=coulumn, r= row, p=player"""
        for i in range(4):
            if not self.check_cell(c,r+i,p):
                return False
        return True

    def check_vertical(self,c,r,p):
        """c=coulumn, r= row, p=player"""
        for i in range(4):
            if not self.check_cell(c+i,r,p):
                return False
        return True

    def check_diagonal_up(self,c,r,p):
        """c=coulumn, r= row, p=player"""
        for i in range(4):
            if not self.check_cell(c+i,r+i,p):
                return False
        return True

    def check_diagonal_down(self,c,r,p):
        """c=coulumn, r= row, p=player"""
        for i in range(4):
            if not self.check_cell(c-i,r+i,p):
                return False
        return True

    def check_win(self,player):
        for c in range(1,7):
            for r in range(1,5):
                if self.check_horizontal(c,r,player):
                    print(player + " Won!")
                    return True
                if c < 4:
                    if self.check_vertical(c,r,player):
                        print(player + " Won!")
                        return True
                    if self.check_diagonal_up(c,r,player):
                        print(player + " Won!")
                        return True
                if c > 3:
                    if self.check_diagonal_down(c,r,player):
                        print(player + " Won!")
                        return True
        return False

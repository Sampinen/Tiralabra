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
        self.running = False
        self.ask()

    def print_board(self):
        output = ""
        for _,line in self.board.items():
            output += "----------------\n"
            for _,value in line.items():
                output += "|" +str(value)
            output +="|\n"
        output += "----------------"
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


    def check_win(self,player):
        for c in range(1,7):
            for r in range(1,5):
                if self.board[c][r] == player and self.board[c][r+1] == player and self.board[c][r+2] == player and self.board[c][r+3] == player:
                    print(player + " Won!")
                    return True
                if c < 4:
                    if self.board[c][r] == player and self.board[c+1][r] == player and self.board[c+2][r] == player and self.board[c+3][r] == player:
                        print(player + " Won!")
                        return True
                    if self.board[c][r] == player and self.board[c+1][r+1] == player and self.board[c+2][r+2] == player and self.board[c+3][r+3] == player:
                        print(player + " Won!")
                        return True
                if c > 3:
                    if self.board[c][r] == player and self.board[c-1][r+1] == player and self.board[c-2][r+2] == player and self.board[c-3][r+3] == player:
                        print(player + " Won!")
                        return True
        return False

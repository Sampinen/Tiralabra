import random

class ConnectFour:
    def __init__(self):
        self.player1= ""
        self.player2 = ""
        self.board = {
        6: {1: (" ",1),2: (" ",2),3: (" ",3), 4: (" ",4), 5:(" ",3), 6:(" ",2),7:(" ",1)},
        5: {1: (" ",2),2: (" ",3),3: (" ",4), 4: (" ",5), 5:(" ",4), 6:(" ",3),7:(" ",2)},
        4: {1: (" ",3),2: (" ",4),3: (" ",5), 4: (" ",6), 5:(" ",5), 6:(" ",4),7:(" ",3)},
        3: {1: (" ",3),2: (" ",4),3: (" ",5), 4: (" ",6), 5:(" ",3), 6:(" ",4),7:(" ",3)},
        2: {1: (" ",2),2: (" ",3),3: (" ",4), 4: (" ",5), 5:(" ",4), 6:(" ",3),7:(" ",2)},
        1: {1: (" ",1),2: (" ",2),3: (" ",3), 4: (" ",4), 5:(" ",3), 6:(" ",2),7:(" ",1)}
        }
        self.played = {1: 0,2: 0,3:0,4: 0,5: 0,6: 0,7: 0}
        self.ask()

    def print_board(self):
        output = ""
        for _,line in self.board.items():
            output += "----------------\n"
            for _,value in line.items():
                output += "|" +str(value[0])
            output +="|\n"
        output += "----------------"
        print(output)

    def play(self,row: int,player):
        if row > 7 or row < 1:
            return print("Valitse numero väliltä 1 ja 7")
        if self.played[row] <6:
            print(self.played[row])
            self.board[self.played[row]+1][row] = (str(player),0)
            self.played[row] +=1
        self.print_board()

    def ask(self):
        player = str(input("Pick a symbol: "))[0]
        while True:
            row = int(input("Pick a row: "))
            self.play(row, player)
            self.play(random.randint(1,7),"P2")
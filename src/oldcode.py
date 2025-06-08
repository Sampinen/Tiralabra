
def check_horizontal(self,c,r,p):
    """c=column, r= row, p=player"""
    score = 0
   
    for i in range(4):
        cell = self.check_cell(c,r+i,p)
        if cell == -1:
            return -1
        score += cell
    return score

def check_vertical(self,c,r,p):
    """c=coulumn, r= row, p=player"""
    score = 0
    for i in range(4):
        cell = self.check_cell(c+i,r,p)
        if cell == -1:
            return -1
        score += cell
    return score

def check_diagonal_up(self,c,r,p):
    """c=coulumn, r= row, p=player"""
    score = 0
    for i in range(4):
        cell = self.check_cell(c+i,r+i,p)
        if cell == -1:
            return -1
        score += cell
    return score

def check_diagonal_down(self,c,r,p):
    """c=coulumn, r= row, p=player"""
    score = 0
    for i in range(4):
        cell = self.check_cell(c-i,r+i,p)
        if cell == -1:
            return -1
        score += cell
    return score

def check_win(self,player):
    for c in range(1,7):
        for r in range(1,5):
            if self.check_horizontal(c,r,player) ==4:
                print(player + " Won!")
                return True
            if c < 4:
                if self.check_vertical(c,r,player) ==4:
                    print(player + " Won!")
                    return True
                if self.check_diagonal_up(c,r,player)==4:
                    print(player + " Won!")
                    return True
            if c > 3:
                if self.check_diagonal_down(c,r,player)==4:
                    print(player + " Won!")
                    return True
    return False

def check_score_cell(self,column,row,player):
    score = -9999
    minr = max(row-3,1)
    maxr = min(row+1,5)                                                                                                                                                                                                                                                                                                   
    minc = max(column-3,1)
    maxc = min(column+1,4)
    for c in range(minc,maxc):
        vertical = self.check_vertical(c,row,player)
        score = max(vertical,score)
    for r in range(minr,maxr):
        horizontal = self.check_horizontal(column,r,player)
        score =max(horizontal,score)
    for i in range(0,4):
        if column+i in range(1,4) and row+i in range(1,5):
            diagonalu= self.check_diagonal_up(column+i,row+i,player)
            score = max(diagonalu,score)
        if column-i in range(4,7) and row+i in range(1,5):
            diagonald = self.check_diagonal_down(column-i,row+i,player)
            score = max(diagonald,score)
        if i>0:
            if column-i in range(1,4) and row-i in range(1,5):
                diagonalu= self.check_diagonal_up(column-i,row-i,player)
                score = max(diagonalu,score)
            if column+i in range(4,7) and row-i in range(1,5):
                diagonald = self.check_diagonal_down(column+i,row-i,player)
                score = max(diagonald,score)
    return score


def check_weights(self,player):
    weight = -99999
    row = 0
    for r in range(1,8):
        if self.played[r] == 6:
            pass
        else:
            column = self.played[r]+1
            if self.weights[column][r] > weight:
                weight = self.weights[column][r]
                row = r
    if row == 0:
        print("Kaikki ruudut täynnä")
    else:
        self.play(row,player)

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


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



def check_scores2(self,p,board):
    score = -99999999
    newroworder = []
    for r in self.roworder:
        if self.played[r] >= self.columncount:
            print("remove "+str(r))
            self.roworder.remove(r)
        else:
            c = self.played[r]+1
            score1 = self.check_score_diagonal_down(c,r,p,board)
            score2 = self.check_score_diagonal_up(c,r,p,board)
            score3 = self.check_score_horizontal(c,r,p,board)
            score4 = self.check_score_vertical(c,r,p,board)
            scoresum = score1+score2+score3+score4
            newroworder.append((r,scoresum))
        newroworder.sort(key=lambda x:x[1],reverse=True)
    print(newroworder)

    def check_score_horizontal(self,c,r,p,board):
        score = 0
        i = 1
        emptyorp = 0 #empty or player
        while i >= 1:
            if self.is_valid_location(c,r+i):
                if board[c][r+i] == p:
                    score +=1
                    emptyorp += 1
                    i += 1
                elif board[c][r+i] != "  ":
                    i = -1
                else:
                    i += 1
                    emptyorp +=1
            else:
                i = -1
        while i < 0:
            if self.is_valid_location(c,r+i):
                if board[c][r+i] == p:
                    score += 1
                    i -= 1
                elif board[c][r+i] == "  ":
                    i -=1
                elif board[c][r+i] != "  " and emptyorp <3:
                    #It is no longer possible to get horizontal win
                    score = -1
                    i = 0
                else:
                    i = 0
            else:
                i = 0
            return self.return_points(score)


    def check_score_vertical(self,c,r,p,board):
        score = 0
        i = -1
        while i < 0:
            if self.is_valid_location(c+i,r):
                if board[c+i][r] == p:
                    score += 1
                    i -= 1
                elif board[c+i][r] == "  ":
                    i -= 1
                else:
                    i = 0
            else:
                i = 0
        return self.return_points(score)

    def check_score_diagonal_down(self,c,r,p,board):
        score = 0
        i = 1
        emptyorp = 0
        while i >= 1:
            if self.is_valid_location(c-i,r+i):
                if board[c-i][r+i] == p:
                    score +=1
                    i += 1
                    emptyorp +=1
                elif board[c-i][r+i]==p:
                    i +=1
                else:
                    i = -1
            else:
                i = -1
        while i < 0:
            if self.is_valid_location(c-i,r+i):
                if board[c-i][r+i] == p:
                    score += 1
                    i -= 1
                elif board[c-i][r+i] == "  ":
                    i -= 1
                elif emptyorp <3:
                    score = -1
                    i = 0
                else:
                    i = 0
            else:
                i = 0
        return self.return_points(score)

    def check_score_diagonal_up(self,c,r,p,board):
        score = 0
        i = 0
        emptyorp = 0
        while i in range(1,4):
            if self.is_valid_location(c+i,r+i):
                if board[c+i][r+i] == p:
                    emptyorp += 1
                    score +=1
                    i += 1
                elif board[c+i][r+i] == "  ":
                    emptyorp +=1
                    i += 1
                else:
                    i = 0
            else:
                i = -1
        while i in range(-4,-1):
            if self.is_valid_location(c+i,r+i):
                if board[c+i][r+i] == p:
                    score += 1
                    emptyorp +=1
                    i -= 1
                else:
                    i = 0
            else:
                i = 0
        return self.return_points(score)


    def return_points(self,score):
        if score ==2:
            return 10
        if score == 3:
            return 99999
        else:
            return 0
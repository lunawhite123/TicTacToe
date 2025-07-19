




class WrongCell(Exception):
    def __init__(self, message):
        super().__init__(message)



class Board:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]

    def __getitem__(self,indx):
        return self.board[indx]
        
    def __str__(self):
        result = []
        for i in self.board:
            result.append(' '.join(map(str,i)))  
        return '\n'.join(result)

class Player:
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol
        self.wins = 0
        self.loses = 0
        self.draws = 0



class Game:
    def __init__(self,board,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.board = board
        
    def start_game(self):
        res = input("Start game? Yes/No").strip().lower()
            
        if res == 'yes':
            board = Board()
            player1 = Player(input("Enter your player name: "), "X")
            player2 = Player(input("Enter your player name: "), "O")
            game = Game(board,player1,player2)
            self.game()
            
        else:
            return "Game not started"

    def game(self):
        current_player = self.player1
        while not self.check_result():
            try:
                row = int(input("Enter line: (0, 2): "))
                col = int(input("Enter column: (0, 2): "))
                self.turn(current_player,row,col)
                current_player = self.player2 if current_player == self.player1 else self.player1
                print(self.board)
            except (ValueError, IndexError):
                print("Wrong value or index")
                continue
            except WrongCell:
                print(WrongCell)
                continue
            
        print(self.check_result)

    def turn(self,player,indx):
        if self.board.getitem[indx] != ' ': 
            raise WrongCell('This cell is already taken')
        else:
            self.board[indx] = player.symbol
        
    def check_win(self,player):
            # проверка строк и столбцов
        for index,lst in enumerate(self.board):
            if all(cell == player.symbol for cell in lst):
                return f'{player} Win!'
            elif self.board[0][index] == player.symbol and self.board[1][index] == player.symbol and self.board[2][index] == player.symbol:
                return f'{player} Win!'
            # проверка диагоналей
        if self.board[0][0] == player.symbol and self.board [1][1] == player.symbol and self.board [2][2] == player.symbol:
            return f'{player} Win!'
        elif self.board[0][2] == player.symbol and self.board [1][1] == player.symbol and self.board [2][0] == player.symbol:
            return f'{player} Win!'
        return None
        
    def check_draw(self):
        for i in self.board:
            if not all(cell == ' ' for cell in i):
                return False
        return True
            
    def check_result(self):
        for i in self.board:
            if not all(cell == ' ' for cell in i):
                return None
        player1_win = self.check_win(self.player1)
        player2_win = self.check_win(self.player2)
            
        if player1_win:
            self.player1.wins += 1
            self.player2.loses += 1
            return player1_win
        elif player2_win:
            self.player2.wins += 1
            self.player1.loses += 1
            return player2_win
        elif self.check_draw():
            self.player1.draws += 1
            self.player2.draws += 1
            return "Draw, today nobody wins!"
            

if __name__=="__main__":
    Game.start_game()
    

















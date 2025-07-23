import pygame
import sys
import logging
from pathlib import Path

pygame.init()

logging.basicConfig(
    filename='TicTacToe.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%Y %H-%M-%S',
    encoding='utf-8'
)







class WrongCell(Exception):
        def __init__(self, message):
            super().__init__(message)

class Board:
    def __init__(self):
        self.board = [[' ' for i in range(3)] for j in range(3)]

    def __setitem__(self,indx, value):
        if isinstance(indx, tuple):
            row,col = indx
            self.board[row][col] = value

    def __getitem__(self, indx):
        if isinstance(indx, tuple):
            row, col = indx
            return self.board[row][col]
        else:
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
    def __init__(self,board):
        self.board = board
        self.player1 = None
        self.player2 = None
        self.current_player = None

    def start_game(self):
        result = None
        #DATA
        # Pictures
        image = pygame.image.load('C:/Users/luna/Pictures/tictactoe1.png')
        image = pygame.transform.scale(image, (800, 600))
        image1 = pygame.image.load('C:/Users/luna/Pictures/tictactoe.png')
        image1 = pygame.transform.scale(image1, (800, 600))
        # Screen
        screen = pygame.display.set_mode((800,600)) 
        pygame.display.set_caption("TicTacToe")
        # Colors
        white = 255, 255, 255
        black = 0,0,0
        Aquamarine = 127, 255, 212
        DarkSlateGray = 47, 79, 79
        DarkKhaki = 189, 183, 107
        SteelBlue = 70, 130, 180
        #RECTS
        rect_tictactoe = pygame.Rect(100,75, 300,300)
        start_game_rect = pygame.Rect(220, 200, 300, 70)
        start_game_rect1 = pygame.Rect(100, 10, 500, 70)
        game_over_rect = pygame.Rect(200,150,400,300)
        #FONTS
        font = pygame.font.SysFont("Arial", 20)
        font_enter_name = pygame.font.SysFont("Arial", 24)
#RENDER FONTS
        text_start_game = font.render("Start Game", True, white)
        text_enter_name = font_enter_name.render("Enter your nickname: ", True, black)
        text_game_over = font_enter_name.render("GAME OVER", True, black)
        text_exit = font_enter_name.render('Press Escape to exit', True, black)
        text_restart = font_enter_name.render("Press R to restart", True, black)
        game_over_print = [text_game_over,text_exit,text_restart]
        #PLAYERS
        player1_name = ""
        player2_name = ""
        #print coord
        text_positions = [
        (game_over_rect.x + 80, game_over_rect.y + 50),   # GAME OVER!
        (game_over_rect.x + 80, game_over_rect.y + 120),  # Press Escape to exit
        (game_over_rect.x + 80, game_over_rect.y + 160)
        ]
        #clock
        clock = pygame.time.Clock()
        #AI
        start_game_rect_ai = pygame.Rect(220, 300, 300, 50)
        text_ai = font.render("Play vs AI", True, white)

        #cells

        cell1 = pygame.Rect(rect_tictactoe.x,rect_tictactoe.y, 100, 100)
        cell2 = pygame.Rect(rect_tictactoe.x + 100,rect_tictactoe.y, 100, 100)
        cell3 = pygame.Rect(rect_tictactoe.x + 200,rect_tictactoe.y, 100, 100)
        cell4 = pygame.Rect(rect_tictactoe.x, rect_tictactoe.y + 100, 100, 100)
        cell5 = pygame.Rect(rect_tictactoe.x + 100,rect_tictactoe.y + 100, 100, 100)
        cell6 = pygame.Rect(rect_tictactoe.x + 200,rect_tictactoe.y + 100, 100, 100)
        cell7 = pygame.Rect(rect_tictactoe.x,rect_tictactoe.y + 200, 100, 100)
        cell8 = pygame.Rect(rect_tictactoe.x + 100,rect_tictactoe.y + 200, 100, 100)
        cell9 = pygame.Rect(rect_tictactoe.x + 200,rect_tictactoe.y + 200, 100, 100)
        cells = [cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]
        cell_to_coords = {
        0: (0, 0), 1: (0, 1), 2: (0, 2),
        3: (1, 0), 4: (1, 1), 5: (1, 2),
        6: (2, 0), 7: (2, 1), 8: (2, 2)}
        
        game_mode = None
        game_state = "menu"
        ##############
        
        while True:

            clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        
                elif game_state == 'menu':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if start_game_rect.collidepoint(event.pos):
                            game_state = 'player1_input'
                        elif start_game_rect_ai.collidepoint(event.pos):
                            game_mode = 'ai'
                            game_state = 'player1_input'

                                
                elif game_state == 'player1_input':
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN and player1_name != '':
                            self.player1 = Player(player1_name, 'X')
                            game_state = 'player2_input'
                        
                        elif event.key == pygame.K_BACKSPACE:
                            player1_name = player1_name[:-1]
                        
                        elif len(player1_name) <= 20 and event.unicode.isprintable():
                            player1_name += event.unicode

                elif game_state == "player2_input" and game_mode == 'ai':
                            player2_name = 'ai'
                            self.player2 = Player(player2_name, 'O')
                            self.current_player = self.player1
                            game_state = "game"

                elif game_state == "player2_input":
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN and player2_name != '':
                                self.player2 = Player(player2_name, 'O')
                                game_state = "game"
                                self.current_player = self.player1
                            elif event.key == pygame.K_BACKSPACE:
                                player2_name = player2_name[:-1]
                            
                            elif len(player2_name) <= 20 and event.unicode.isprintable():
                                player2_name += event.unicode

                elif game_state == 'game' and game_mode != 'ai':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for coord, cell in enumerate(cells):
                            if cell.collidepoint(event.pos):
                                if self.board[cell_to_coords[coord]] == ' ':
                                    self.board[cell_to_coords[coord]] = self.current_player.symbol
                                    result = self.check_result()
                                    if result:
                                        text_game_over = font_enter_name.render(result, True, black)
                                        game_over_print[0] = text_game_over
                                        game_state = "game_over"
                                        logging.info(f'Players: {self.player1.name}, {self.player2.name},\nResult: {result},\nBoard:\n{self.board} ')
                                        self.check_log()
                                        
                                    
                                    self.current_player = self.player2 if self.current_player == self.player1 else self.player1
                                    break
                
                elif game_state == 'game':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.current_player == self.player1:
                            for coord, cell in enumerate(cells):
                                if cell.collidepoint(event.pos):
                                    if self.board[cell_to_coords[coord]] == ' ':
                                        self.board[cell_to_coords[coord]] = self.current_player.symbol
                                        result = self.check_result()
                                        if result:
                                            text_game_over = font_enter_name.render(result, True, black)
                                            game_over_print[0] = text_game_over
                                            game_state = "game_over"
                                            logging.info(f'Players: {self.player1.name}, {self.player2.name},\nResult: {result},\nBoard:\n{self.board} ')
                                            self.check_log()
                                        else:
                                            self.current_player = self.player2
                                            best_move = self.find_best_move()
                                            self.board[best_move] = self.player2.symbol
                                            result = self.check_result()
                                            if result:
                                                text_game_over = font_enter_name.render(result, True, black)
                                                game_over_print[0] = text_game_over
                                                game_state = "game_over"
                                                logging.info(f'Players: {self.player1.name}, {self.player2.name},\nResult: {result},\nBoard:\n{self.board} ')
                                                self.check_log()
                                                
                                            
                                        self.current_player = self.player1
                                        
                                    break
                        
                elif game_state == 'game_over':
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                        self.board = Board()
                        self.player1 = None
                        self.player2 = None
                        self.current_player = None
                        player1_name = ""
                        player2_name = ""
                        game_state = 'menu'
                        text_game_over = font_enter_name.render("GAME OVER", True, black)
                        game_over_print[0] = text_game_over
            
            if game_state == "menu":
                screen.blit(image, (0,0))
                pygame.draw.rect(screen,DarkSlateGray,start_game_rect)
                screen.blit(text_start_game, (start_game_rect.x + 100, start_game_rect.y + 20))
                pygame.draw.rect(screen,(100, 150, 100),start_game_rect_ai)
                screen.blit(text_ai, (start_game_rect_ai.x + 100, start_game_rect_ai.y + 10))

            elif game_state == 'player1_input':
                screen.blit(image1, (0,0))
                pygame.draw.rect(screen, DarkKhaki, start_game_rect1)
                screen.blit(text_enter_name, (start_game_rect1.x + 20, start_game_rect1.y + 20))
                player1_render = font_enter_name.render(player1_name, True, black)
                screen.blit(player1_render, (start_game_rect1.x + 250, start_game_rect1.y + 20))
                 
                                
            elif game_state == 'player2_input':         
                screen.blit(image1, (0,0))
                pygame.draw.rect(screen, DarkKhaki, start_game_rect1)
                screen.blit(text_enter_name, (start_game_rect1.x + 20, start_game_rect1.y + 20))
                player2_render = font_enter_name.render(player2_name, True, black)
                screen.blit(player2_render, (start_game_rect1.x + 250, start_game_rect1.y + 20))
                  

            elif game_state == 'game':
                screen.fill(SteelBlue)
                for cell in cells:
                    pygame.draw.rect(screen,white,cell)
                pygame.draw.rect(screen,white,rect_tictactoe, border_radius=1)
                pygame.draw.line(screen, black, (rect_tictactoe.x + 100, rect_tictactoe.y), (rect_tictactoe.x + 100, rect_tictactoe.y + rect_tictactoe.height), 7)
                pygame.draw.line(screen, black, (rect_tictactoe.x + 200, rect_tictactoe.y), (rect_tictactoe.x + 200, rect_tictactoe.y + rect_tictactoe.height), 7)
                pygame.draw.line(screen, black, (rect_tictactoe.x, rect_tictactoe.y + 100), (rect_tictactoe.x + rect_tictactoe.width, rect_tictactoe.y + 100), 7)
                pygame.draw.line(screen, black, (rect_tictactoe.x, rect_tictactoe.y + 200), (rect_tictactoe.x + rect_tictactoe.width, rect_tictactoe.y + 200), 7)

                if self.current_player:
                    current_text = font.render(f'Turn: {self.current_player.name}({self.current_player.symbol})', True, black)
                    screen.blit(current_text, (450,100))
                for coord, cell in enumerate(cells):
                    symbol = self.board[cell_to_coords[coord]]
                    if symbol != ' ':
                        if symbol == 'O':
                            pygame.draw.circle(screen, black, (cell.x + 50, cell.y + 50), 15, 7)
                                        
                        elif symbol == 'X':
                            pygame.draw.line(screen, black, (cell.x, cell.y), (cell.x + 100, cell.y + 100), 7)
                            pygame.draw.line(screen, black, (cell.x + 100, cell.y), (cell.x, cell.y + 100), 7)
            
            elif game_state == 'game_over':
                screen.fill(SteelBlue)
                pygame.draw.rect(screen,Aquamarine,game_over_rect)
                
                for indx,text in enumerate(game_over_print):
                    screen.blit(text, text_positions[indx])
                    
                
                
            pygame.display.flip()    

    def turn(self,player,indx):
        self.board[indx] = player.symbol
            
    def check_win(self,player):
            # проверка строк и столбцов
        for index,lst in enumerate(self.board):
            if all(cell == player.symbol for cell in lst):
                return f'{player.name} Win!'
            elif self.board[0][index] == player.symbol and self.board[1][index] == player.symbol and self.board[2][index] == player.symbol:
                    return f'{player.name} Win!'
            # проверка диагоналей
        if self.board[0][0] == player.symbol and self.board [1][1] == player.symbol and self.board [2][2] == player.symbol:
            return f'{player.name} Win!'
        elif self.board[0][2] == player.symbol and self.board [1][1] == player.symbol and self.board [2][0] == player.symbol:
            return f'{player.name} Win!'
        return None
            
    def check_draw(self):
        for i in self.board:
            for cell in i:
                if cell == ' ':
                    return False
        return True
                
    def check_result(self):
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
        return None
    
    def check_log(self):
        file = Path('TicTacToe.log')
        
        if file.exists():
            with open(file, 'r', encoding='utf-8') as f:
                file_data = f.readlines()
                
        if len(file_data) > 50:
            file_data = file_data[:-30]
            with open(file, 'w', encoding='utf-8') as f:
                f.writelines(file_data)

    def evaluate(self):
        if self.check_win(self.player2):
            return 10
        elif self.check_win(self.player1):
            return -10
        return 0
    
    def minimax(self,board,depth,is_maximizaing):
        score = self.evaluate()

        if score == 10:
            return score - depth
        if score == -10:
            return score + depth
        
        if self.check_draw():
            return 0
        
        if is_maximizaing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'O'
                        best_score = max(best_score, self.minimax(board, depth+1, False))
                        board[i][j] = ' '
            return best_score

        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = 'X'
                        best_score = min(best_score, self.minimax(board, depth+1, True))
                        board[i][j] = ' '
            return best_score
        
    def find_best_move(self):
        best_val = -1000
        best_move = (-1,-1)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    move_val = self.minimax(self.board, 0, False)
                    self.board[i][j] = ' '

                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move

board = Board()
game = Game(board)
game.start_game()
    
            


    
    
    
        

        









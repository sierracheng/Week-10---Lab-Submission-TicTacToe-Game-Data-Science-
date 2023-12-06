from logic import Game, Player, Bot
import os
def print_board(board):
    for i, row in enumerate(board):
        print_row = [' ' if cell is None else cell for cell in row]
        print(' | '.join(print_row))
        if i < 2:
            print('---+---+---')

def main():
    mode = input("Choose mode (1 for single player, 2 for two players): ")
    player1 = Player('X')
    player2 = Bot('O') if mode == '1' else Player('O')

    game = Game(player1, player2)
    
    if not os.path.exists('game_log_1.csv'):
        with open('game_log_1.csv', 'w') as f:
            f.write('winner,move_count,mode,first_loc\n')
    while True:
        print_board(game.board)
        game.play_turn()
        winner = game.get_winner()
        if winner:
            print_board(game.board)
            print(f"Player {winner} wins!")
            with open('game_log_1.csv', 'a') as f:
                first_loc = game.first_loc[0]*3 + game.first_loc[1]
                f.write(f'{winner},{game.move_count},{mode},{first_loc}\n')
            break
        if game.is_draw():
            print_board(game.board)
            print("It's a draw!")
            with open('game_log_1.csv', 'a') as f:
                first_loc = game.first_loc[0]*3 + game.first_loc[1]
                f.write(f'draw,{game.move_count},{mode},{first_loc}\n')

            break

if __name__ == '__main__':
    main()
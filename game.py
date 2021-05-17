import board

def main():
    """
    main func
    """
    command = ''
    list_of_commands = ['Clear', 'exit', 'Make a move', 'Make computer move', 'Chose the best move']
    Game = board.Board()
    while command != 'exit':
        print(Game)
        print('List of commands:')
        for i in list_of_commands:
            print(i)
        command = input('Enter your command: ')
        if command == 'Clear':
            Game.clear()
        elif command == 'Make a move':
            position = input('Position(like: 1, 2): ')
            turn = input('Symbol(x of 0): ')
            position = (int(position[0]), int(position[-1]))
            try:
                Game.make_move(position, turn)
            except IndexError:
                print('Sorry there is something wrong')
        elif command == 'Make computer move':
            ret = Game.make_computer_move()
            if ret != None:
                print(ret)
        elif command == 'Chose the best move':
            turn = input('Pleas input your symbol(x, 0): ')
            position = Game.chose_next_move(turn)
            print(f'Here is your best move: {position}')
        elif command == 'exit':
            print('By by')
        else:
            print('There is no such command')

if __name__ == "__main__":
    main()
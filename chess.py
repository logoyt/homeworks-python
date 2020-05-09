WHITE = 1
BLACK = 2


def opposite_color(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def check_input(coords):
    coords = coords.split()
    if len(coords) != 4:
        print('Ошибка ввода.')
    return False
    '''
    Задание 1.
    Дописать функцию
    Функция должна проверять корректность ввода
    Вводом должны являться 4 числа со значениями от 1 до 8
    Функция возвращает False, если ввод оказался неправильным
    или список координат, если ввод правильный например [2, 2, 3, 3]
    '''


def print_field(field):
    print('     +----+----+----+----+----+----+----+----+')
    for row in range(7, -1, -1):
        print(' ', row + 1, end='  ')
        for col in range(8):
            print('|', field[row][col], end=' ')
        print('|')
        print('     +----+----+----+----+----+----+----+----+')
    print(end='        ')
    for col in range(8):
        print(col + 1, end='    ')
    print()


def main():
    player_color = WHITE
    field = []
    for i in range(8):
        field.append(['  '] * 8)
    field[6][1] = 'bK' # black King
    field[1][6] = 'wK' # white King
    while True:
        print_field(field)
        print('Команды:')
        print('    exit                          -- выход')
        print('    <row> <col> <row1> <col1>     -- ход из клетки (row, col)')
        print('                                     в клетку (row1, col1)')

        if player_color == WHITE:
            print('Ход белых:')
        else:
            print('Ход чёрных:')
        command = input()
        if command == 'exit':
            break
        else:
            command = check_input(command)
            if command == False:
                print('Попробуйте ещё раз')
            else:
                pass
                '''
                Задание 2.
                Проверить, являются ли первые два введённых числа - координатами
                фигуры текущего цвета. Цвет фигуры можно проверить по первой букве фигуры
                Если игрок выбрал фигуру не своего цвета или пустую клетку - он должен
                походить заново.
                Если первая координата (первые два числа) введены правильно, то проверяется
                вторая координата. Так как фигуры - короли, то они могут передвигаться
                только на одну клетку от своего текущего местоположения. Если игрок пытается
                передвинуть своего короля дальше, чем на одну клетку, написать, что так нельзя
                и начать его ход заново, иначе передвинуть короля и поменять цвет текущего 
                игрока с помощью функции opposite_color().
                '''


main()

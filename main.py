import random

GREEN = '\033[32m'
YELLOW = '\033[33m'
WHITE = '\033[37m'


class Cell:
    def __init__(self):
        self.field = '#'
        self.color = '\033[37m'

    def print_field(self):
        print(self.color + self.field, end='')


def set_white_color():
    print(WHITE, end='')


def greetings():
    print(GREEN + 'Приветствую вас в консольной версии игры Сапёр!')


def input_start():
    print(GREEN + 'Если хотите начать новую игру - введите \'new\'')
    print('Если хотите загрузить игру - введите \'load <path>\', где path - путь до игры на вашем компьютере')
    print('Если хотите выйти из игры - введите \'exit\'')


def input_dimensions():
    print(GREEN +
          'Введите параметры поля в формате \'n m k\', где n - число строк, m - число столбцов, k - число мин')


def input_move():
    print(GREEN + '\'Open X Y\' - открыть клетку с координатами (X, Y)')
    print('\'Flag X Y\' - поставить флажок в клетку с координатами (X, Y)')


def error_input():
    print(YELLOW + 'Данные были введены в неверном формате или сами данные некорректны.\nПопробуйте ещё раз.')


def error_dimension():
    print(YELLOW + 'Никакая из размерностей не может быть равна нулю и число мин не может быть равно нулю')


def error_extra_mines():
    print(YELLOW + 'число мин не может превышать размера поля')


def end():
    print(GREEN + 'Спасибо за игру!')


def can_open(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j].field == '#':
                return True
    return False


def print_all_field(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            field[i][j].print_field()
        print()


def main():
    greetings()
    while True:
        input_start()

        command = input().split(' ')
        if command[0].lower() == 'new' and len(command) == 1:
            flag = True
            while flag:
                flag = False
                input_dimensions()
                parameters = input().split()
                if len(parameters) != 3 or not parameters[0].isnumeric() or not parameters[1].isnumeric() or not \
                        parameters[2].isnumeric():
                    flag = True
                    error_input()
                    continue
                n, m, mines = map(int, parameters)
                if n == 0 or m == 0:
                    flag = True
                    error_dimension()
                    continue
                elif mines > n * m:
                    flag = True
                    error_extra_mines()
                    continue
            player_field = [[Cell()] * n for i in range(m)]
            flags_left = mines
            while can_open(player_field):
                print_all_field(player_field)
                input_move()
                command = input().split()




        elif command[0].lower() == 'load' and len(command) == 2:
            pass
        elif command[0].lower() == 'exit' and len(command) == 1:
            end()
            break
        else:
            error_input()


if __name__ == '__main__':
    main()

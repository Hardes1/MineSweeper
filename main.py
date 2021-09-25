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


def actions_before_start():
    print(GREEN + 'Если хотите начать новую игру - введите \'new\'')
    print('Если хотите загрузить игру - введите \'load <path>\', где path - путь до игры на вашем компьютере')
    print('Если хотите выйти из игры - введите \'exit\'')


def error_input():
    print(YELLOW + 'Данные были введены в неверном формате или сами данные некорректны.\nПопробуйте ещё раз.')


def error_dimension():
    print(YELLOW + 'Никакая из размерностей не может быть равна нулю и число мин не может быть равно нулю')


def error_extra_mines():
    print(YELLOW + 'число мин не может превышать размера поля')


def end():
    print(GREEN + 'Спасибо за игру!')


def main():
    greetings()
    while True:
        actions_before_start()

        command = input().split(' ')
        if command[0].lower() == 'new':
            flag = True
            while flag:
                flag = False
                print(GREEN +
                      'Введите параметры поля в формате \'n m k\', где n - число строк, m - число столбцов, k - число мин')
                parameters = input().split()
                if len(parameters) != 3 or not parameters[0].isnumeric() or not parameters[1].isnumeric() or not \
                        parameters[2].isnumeric():
                    flag = True
                    error_input()
                    continue
                n, m, k = map(int, parameters)
                if n == 0 or m == 0 or k == 0:
                    flag = True
                    error_dimension()
                    continue
                elif k > n * m:
                    flag = True
                    error_extra_mines()
                    continue
        elif command[0].lower() == 'load':
            pass
        elif command[0].lower() == 'exit':
            end()
            break
        else:
            error_input()


if __name__ == '__main__':
    main()

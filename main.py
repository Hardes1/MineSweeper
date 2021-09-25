GREEN = '\033[32m'
WHITE = '\033[37m'


def set_color(color):
    print(color, end='')


def greetings():
    print(GREEN + 'Приветствую вас в консольной версии игры Сапёр!')


def actions_before_start():
    print('Если хотите начать новую игру - введите ''new''')
    print('Если хотите загрузить игру - введите ''load <path>'', где path - путь до игры на вашем компьютере')
    print('Если хотите выйти из игры - введите ''exit''')


def main():
    greetings()
    while True:
        actions_before_start()
        s = input().split(' ')
        if s[0].lower() == 'new':
            pass
        elif s[0].lower() == 'load':
            pass
        elif s[0].lower() == 'exit':
            break
        else:
            print('Была введена некорректная команда, попробуйте ещё раз')


if __name__ == '__main__':
    main()

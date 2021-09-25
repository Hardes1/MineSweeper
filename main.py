import random
from collections import deque

GREEN = '\033[32m'
YELLOW = '\033[33m'
WHITE = '\033[37m'
RED = '\033[31m'


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
          'Введите параметры поля в формате \'n m k\', где n - число строк, m - число столбцов, k - число мин.')
    print('1<=n<=255, 1<=m<=255, 0<=k<n*n')


def input_move():
    print(GREEN + '\'Open X Y\' - открыть клетку с координатами (X, Y).')
    print('\'Flag X Y\' - поставить флажок в клетку с координатами (X, Y).')
    print('\'Remove X Y\' - удалить флажок из клетки с координатами (X, Y).')


def error_input():
    print(YELLOW + 'Данные были введены в неверном формате или сами данные некорректны.\nПопробуйте ещё раз.')


def error_set_flag():
    print(YELLOW + 'Невозможно поставить флаг в выбранную клетку.')


def error_dimension():
    print(YELLOW + 'Никакая из размерностей не может быть равна нулю.')


def error_open():
    print(YELLOW + 'Выбранная клетка уже открыта')


def error_no_flags():
    print(YELLOW + 'Вы не можете больше поставить флаги, так как они закончились.')


def error_extra_mines():
    print(YELLOW + 'Число мин не может превышать размера поля')


def error_no_flags_here():
    print(YELLOW + 'В данной клетке нет флага.')


def error_border():
    print(YELLOW + 'Выбранная клетка выходит за границы поля.')


def error_zero_step():
    print(YELLOW + 'Нельзя ставить флаг на нулевом шаге.')


def end():
    print(GREEN + 'Спасибо за игру!')


def can_open_any(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == '*':
                return 0
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == '#':
                return 2
    return 1


def print_all_field(field):
    for i in range(len(field) - 1, -1, -1):
        for j in range(len(field[i])):
            if field[i][j] == '.' or field[i][j].isnumeric() or field[i][j] == '#':
                print(WHITE + field[i][j], end='')
            elif field[i][j] == '*':
                print(RED + field[i][j], end='')
            else:
                print(YELLOW + field[i][j], end='')
        print()


def check_borders(x, y, n, m):
    return 0 <= x < m and 0 <= y < n


def check_mines(field):
    for i in range(len(field)):
        for elem in field[i]:
            if elem == '*':
                return True
    return False


def lose():
    print(RED + 'Вы проиграли!')


def win():
    print(GREEN + 'Поздравляем, вы победили!')


def again():
    print(GREEN + 'Если хотите в главное меню введите \'main\'')
    print('Если хотите завершить работу программы введите что угодно, кроме \'main\'')


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
                if n <= 0 or m <= 0 or mines < 0 or n > 255 or n > 255:
                    flag = True
                    error_dimension()
                    continue
                elif mines >= n * m:
                    flag = True
                    error_extra_mines()
                    continue
            player_field = [['#'] * m for i in range(n)]
            mines_field = [['.'] * m for i in range(n)]
            flags_left = mines
            step = 0
            while can_open_any(player_field) > 1:
                print_all_field(player_field)
                input_move()
                command = input().split()
                if len(command) != 3:
                    error_input()

                elif command[0].lower() == 'open' and command[1].isnumeric() and command[2].isnumeric():
                    x, y = int(command[1]), int(command[2])
                    x -= 1
                    y -= 1
                    if not check_borders(x, y, n, m):
                        error_border()
                        continue
                    elif player_field[y][x] != '#' and player_field[y][x] != 'F':
                        error_open()
                        continue
                    if step == 0:
                        a = []
                        for i in range(n):
                            for j in range(m):
                                if i != y or j != x:
                                    a.append((i, j))
                        random.shuffle(a)
                        for i in range(mines):
                            mines_field[a[i][0]][a[i][1]] = '*'
                        for i in range(n):
                            for j in range(m):
                                if mines_field[i][j] == '.':
                                    cnt = 0
                                    for di in range(-1, 2):
                                        for dj in range(-1, 2):
                                            if check_borders(j + dj, i + di, n, m) and mines_field[i + di][
                                                j + dj] == '*':
                                                cnt += 1
                                    if cnt > 0:
                                        mines_field[i][j] = str(cnt)
                    if player_field[y][x] == 'F':
                        player_field[y][x] = '#'
                        flags_left += 1
                    q = deque()
                    s = set()
                    q.append((y, x))
                    s.add((y, x))
                    while len(q) > 0:
                        y, x = q.popleft()
                        s.remove((y, x))
                        player_field[y][x] = mines_field[y][x]
                        if player_field[y][x] == '.':
                            for di in range(-1, 2):
                                for dj in range(-1, 2):
                                    if check_borders(x + dj, y + di, n, m) and mines_field[y + di][
                                        x + dj] != '*' and player_field[y + di][x + dj] == '#' and (
                                            y + di, x + dj) not in s:
                                        q.append((y + di, x + dj))
                                        s.add((y + di, x + dj))
                    step += 1
                elif command[0].lower() == 'flag' and command[1].isnumeric() and command[2].isnumeric():
                    x, y = int(command[1]), int(command[2])
                    x -= 1
                    y -= 1

                    if not check_borders(x, y, n, m):
                        error_border()
                        continue
                    elif player_field[y][x] != '#':
                        error_set_flag()
                        continue
                    elif flags_left == 0:
                        error_no_flags()
                        continue
                    elif step == 0:
                        error_zero_step()
                        continue
                    player_field[y][x] = 'F'
                    flags_left -= 1
                elif command[0].lower() == 'remove' and command[1].isnumeric() and command[2].isnumeric():
                    x, y = int(command[1]), int(command[2])
                    x -= 1
                    y -= 1
                    if not check_borders(x, y, n, m):
                        error_border()
                        continue
                    elif player_field[y][x] != 'F':
                        error_no_flags_here()
                        continue
                    player_field[y][x] = '#'
                    flags_left += 1
                else:
                    error_input()

            if can_open_any(player_field) == 1:
                win()
                print_all_field(player_field)
            elif can_open_any(player_field) == 0:
                lose()
                for i in range(n):
                    for j in range(m):
                        if mines_field[i][j] == '*':
                            player_field[i][j] = '*'
                print_all_field(player_field)
            again()
            command = input()
            if command.lower() != 'main':
                return
        elif command[0].lower() == 'load' and len(command) == 2:
            pass

        elif command[0].lower() == 'exit' and len(command) == 1:
            end()
            break
        else:
            error_input()


if __name__ == '__main__':
    main()
    print(WHITE + 'Спасибо за игру!')

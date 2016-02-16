from __future__ import print_function

matrix = [[-1 for x in range(3)] for x in range(3)]
matrix_x = 3
matrix_y = 3

my_dict = {-1: ' ', 0: 'O', 1: 'X'}


def main():
    print('WELCOME TO THE TIC TAC TOE!')
    has_finished = 0
    while not has_finished:
        result = 0
        while not result:
            print_matrix()
            first_x = input('1st player - Enter X position: ')
            first_y = input('1st player - Enter Y position: ')
            result = add_to_matrix(first_y - 1, first_x - 1, 1)
        result = 0
        while not result:
            print_matrix()
            second_x = input('2nd player - Enter X position: ')
            second_y = input('2nd player - Enter Y position: ')
            result = add_to_matrix(second_y - 1, second_x - 1, 0)
        has_finished = check_matrix()


def print_matrix():
    print('This is the state of the table:')
    for i in range(matrix_x):
        print(' - - -')
        print('|', end='')
        for j in range(matrix_y):
            print(my_dict[matrix[i][j]], end='')
            print('|', end='')
        print()
    print(' - - -')


def add_to_matrix(i, j, value):
    try:
        if matrix[i][j] == -1:
            matrix[i][j] = value
            return 1
        else:
            print('ERROR: That coordinate is already used.')
            return 0
    except IndexError:
        print("ERROR: That coordinate isn't in range.")
        return 0


def check_matrix():
    result = 1
    for i in range(matrix_x):
        for j in range(matrix_y):
            if matrix[i][j] == -1:
                result = 0
    return result


if __name__ == "__main__":
    main()

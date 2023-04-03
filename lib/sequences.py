#!/usr/bin/env python3

# def print_fibonacci(length):
#     fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#     print(fibonacci[0: int(length)])


def print_fibonacci(length):
    if length <= 0:
        print([])
        return

    fibonacci_array = [0, 1]

    if length == 1:
            print([0])
    elif length == 2:
        print(fibonacci_array)
    else:
        for i in range(2, length):
                next_num = fibonacci_array[-1] + fibonacci_array[-2]
                fibonacci_array.append(next_num)
        print(fibonacci_array)
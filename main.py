import sys
import threading
import os
import numpy as np

c = 0


def aray(size, numbers):

    splitted = numbers.split()
    arr1 = np.zeros(int(size))
    i, k, start = 0, 1, 0
    for a in range(arr1.size):
        arr1[i] = int(splitted[i])
        if arr1[i] == -1:
            start = i
        i += 1
    check(k, start, arr1)


def check(k, start, arr1):

    global c
    for i in range(arr1.size):
        if arr1[i] == start:
            move = i
            k += 1
            if c < k:
                c = k
            k = check(k, move, arr1)
    k -= 1
    return k

def main():

    first_input = input()
    if first_input.__contains__('I'):
        second_input = input()
        third_input = input()
        aray(second_input, third_input)
    elif first_input.__contains__('F'):
        file_name = input()
        if os.path.exists(file_name):
            file = os.path.join(os.getcwd(), 'test', file_name)
            with open(file, 'r') as f:
                second_input = f.readline()
                third_input = str(f.readline())
                aray(second_input, third_input)
        else:
            print("INPUT-OUTPUT ERROR")
            return
    else:
        print("INPUT-OUTPUT ERROR")
        return
    print(c)


if __name__ == "__main__":
    main()

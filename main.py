import os
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def check(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    stack = []
    for i, next in enumerate(text):
        if next in "([{":
            stack.append(Bracket(next, i+1))
        if next in ")]}":
            if not stack or not check(stack[-1].char, next):
                return i+1
            stack.pop()
    if stack:
        return stack[0].position
    return "Success"


def main():
    first_input = input()
    if first_input.__contains__('I'):
        text_line = input()
    elif first_input.__contains__('F'):
        file_name = input()
        if os.path.exists(file_name):
            with open(file_name) as file:
                text_line = file.read()
        else:
            print("INPUT-OUTPUT ERROR")
            return
    else:
        print("INPUT-OUTPUT ERROR")
        return
    output = find_mismatch(text_line)
    print(output)


if __name__ == "__main__":
    main()

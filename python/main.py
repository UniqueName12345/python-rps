#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: ./brainfuck.py <file>")
        return
    try:
        with open(sys.argv[1], 'r') as f:
            code = f.read()
    except IOError:
        print("Error: Can't read file")
        return
    code = clean_code(code)
    if not code:
        print("Error: No code to execute")
        return
    execute(code)


def clean_code(code):
    """
    Remove all non-brainfuck characters from the code
    """
    return ''.join(filter(lambda x: x in '><+-.,[]', code))


def execute(code):
    """
    Execute the brainfuck code
    """
    code_ptr = 0
    data_ptr = 0
    data = [0]
    loop_stack = []
    while code_ptr < len(code):
        c = code[code_ptr]
        if c == '>':
            data_ptr += 1
            if data_ptr == len(data):
                data.append(0)
        elif c == '<':
            data_ptr = 0 if data_ptr <= 0 else data_ptr - 1
        elif c == '+':
            data[data_ptr] = 0 if data[data_ptr] == 255 else data[data_ptr] + 1
        elif c == '-':
            data[data_ptr] = 255 if data[data_ptr] == 0 else data[data_ptr] - 1
        elif c == '.':
            sys.stdout.write(chr(data[data_ptr]))
        elif c == ',':
            data[data_ptr] = ord(sys.stdin.read(1))
        elif c == '[':
            if data[data_ptr] == 0:
                loop_level = 1
                while loop_level > 0:
                    code_ptr += 1
                    if code[code_ptr] == '[':
                        loop_level += 1
                    elif code[code_ptr] == ']':
                        loop_level -= 1
            else:
                loop_stack.append(code_ptr)
        elif c == ']':
            code_ptr = loop_stack.pop() - 1
        code_ptr += 1


if __name__ == '__main__':
    main()
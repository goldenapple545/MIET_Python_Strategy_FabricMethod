#!/usr/bin/python3


from Context import Context
from Strategy import *
from WindowFactory import MainWindowFactory


def start():
    window = MainWindowFactory().create_window()
    context = Context(FileStrategy('log.txt'))
    window.show(context)


if __name__ == '__main__':
    start()

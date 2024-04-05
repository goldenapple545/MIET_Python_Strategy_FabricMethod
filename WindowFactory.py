#!/usr/bin/python3

from abc import ABC, abstractmethod
from Windows import *


class WindowFactory(ABC):
    @abstractmethod
    def create_window(self):
        pass


class MainWindowFactory(WindowFactory):
    def create_window(self):
        return MainWindow()


class OptionsWindowFactory(WindowFactory):
    def create_window(self):
        return OptionsWindow()


class ResultWindowFactory(WindowFactory):
    def create_window(self):
        return ResultWindow()

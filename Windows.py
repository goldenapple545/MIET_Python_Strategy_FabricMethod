#!/usr/bin/python3

import PySimpleGUI as sg

import WindowFactory
from WindowFactory import *


class Window:
    def show(self):
        pass


class MainWindow(Window):
    def __init__(self):
        self.layout = [
            [sg.Text('Input time:')],
            [sg.Input(key='-INPUT-')],
            [sg.Button('Convert')],
            [sg.Button('Reset', key='-RESET-')]
        ]

    def show(self, context):
        window = sg.Window('Time', self.layout)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Convert':
                try:
                    int(values['-INPUT-'])
                except:
                    continue
                options_window = WindowFactory.OptionsWindowFactory().create_window()
                options_window.show(values['-INPUT-'], context)
                context.send_message(f"User input: {values['-INPUT-']}")
            elif event == '-RESET-':
                window['-INPUT-'].update(value='')
        window.close()


class OptionsWindow(Window):
    def __init__(self):
        self.layout = [
            [sg.Text('Choose convert to:')],
            [sg.Combo(['Seconds in minutes', 'Minutes in hours', 'Hours in days'], key='-OPTION-',
                      default_value='Seconds in minutes')],
            [sg.Button('Choose')]
        ]

    def show(self, text, context):
        window = sg.Window('Format', self.layout)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == 'Choose':
                result_window = WindowFactory.ResultWindowFactory().create_window()
                result_window.show(text, values['-OPTION-'], context)
                context.send_message(f"User option: {values['-OPTION-']}")
        window.close()


class ResultWindow(Window):
    def __init__(self):

        self.layout = [
            [sg.Text('Result:', size=(15, 1), justification='center')],
            [sg.Text(size=(40, 1), key='-RESULT-')],
            [sg.Button('Calculate')]
        ]

    def show(self, text, option, context):
        window = sg.Window('Result', self.layout)
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Calculate':
                if option == 'Seconds in minutes':
                    result = int(text) // 60
                elif option == 'Minutes in hours':
                    result = int(text) // 60
                elif option == 'Hours in days':
                    result = int(text) // 24
                window['-RESULT-'].update(result)
                context.send_message(f"Calculated Result: {result}")
        window.close()

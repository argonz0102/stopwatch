from pydoc import visiblename
from xml.dom.minidom import Element
import PySimpleGUI as sg
from time import time

def create_window():

    sg.theme('Black')
    layout = [
        [sg.Push(), sg.Button('Lukk', pad = 0, enable_events = True, key = '-Close-', button_color = '#FF0000', border_width = 0)],
        [sg.VPush()],
        [sg.Text('Tid', font = 'Young 50', key = '-Time-')],
        [sg.Button('Start', button_color = ('#FFFFFF', '#FF0000'), border_width = 0, key = '-Startstop-' ), sg.Button('Lap', button_color = ('#FFFFFF', '#FF0000'), border_width = 0, key = '-Lap-', visible = False)],
        [sg.Column([[]], key = '-Laps-')],
        [sg.VPush()]


    ]

    return sg.Window('Stopwatch',layout, size = (300,300), no_titlebar = True, element_justification = 'center')


window = create_window()
start_time = 0
active = False
lap_amount = 1

while True:
    event, values = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, '-Close-'):
        break
    if event == '-Startstop-':
        if active:
            active = False
            window['-Startstop-'].update('Reset')
            window['-Lap-'].update(visible = False)
        else:

            if start_time > 0:
                window.close()
                window = create_window()
                start_time = 0
                lap_amount = 1

            else:
                start_time = time()
                active = True
                window['-Startstop-'].update('Stop')
                window['-Lap-'].update(visible = True)

    if active:
        elapsed_time = round(time() - start_time,1)
        window['-Time-'].update(elapsed_time)

    if event == '-Lap-':
        window.extend_layout(window['-Laps-'], [[sg.Text(lap_amount), sg.VSeparator(), sg.Text(elapsed_time)]])
        lap_amount += 1
window.close()
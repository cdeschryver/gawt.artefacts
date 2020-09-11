import PySimpleGUI as sg
import numpy as np
import math
import matplotlib.pyplot as plt

sg.theme('DarkAmber')

layout = [
        #[sg.Canvas(size=(640, 480), key='canvas')],
        [sg.Frame('Erwartungswert',[[
            sg.Slider(range=(-5, 5), orientation='h', size=(40, 20), default_value=0, resolution = .5, enable_events=True),
        ]]),
        sg.Frame('Varianz',[[
            sg.Slider(range=(0.1, 5), orientation='h', size=(40, 20), default_value=0.5, resolution= .1, enable_events=True),
        ]])],
        [sg.Checkbox('Track'), sg.Button('Clear'), sg.Button('Close')]
         ]


# Create the Window
window = sg.Window('Gaußverteilung', layout , keep_on_top = True, finalize = True) #, no_titlebar=True
# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close':	# if user closes window or clicks cancel
        break
    if event == 'Clear':
        plt.clf()
    if values[2] == False:
        plt.clf()
    #print('Erwartungswert: ', values[0])
    #print("Varianz: ", values[1])
    mue = values[0]  # Erwartungswert
    var = values[1]  # Varianz
    dev = math.sqrt(var)  # Standardabweichung
    X = np.linspace(mue - 5, mue + 5, 500, endpoint=True)  # Berechnung x-Werte
    F = (1 / (dev * math.sqrt(2 * np.pi))) * np.e ** ((-1 / 2) * (((X - mue) / dev) ** 2))  # Berechnung Gaussverteilung
    plt.plot(X, F)
    startx, endx = mue - 5, mue + 5
    starty, endy = -0.1, 1
    plt.axis([startx, endx, starty, endy])

    fig = plt.gcf()  # Grabs the current figure
    fig.show()

window.close()

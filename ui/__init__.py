import PySimpleGUI as sg
from calculations import *


def neutron_interaction_options():
    return list(delta_map.keys())


if __name__ == "__main__":
    layout = [
        [sg.Text("Select state of aggregation", font=("Arial", 15))],
        [sg.Radio("solid", "SOARADIO", enable_events=True, default=True, key='solid', font=("Arial", 15))],
        [sg.Radio("gas", "SOARADIO", enable_events=True, key='gas', font=("Arial", 15))],
        [sg.Radio("liquid", "SOARADIO", enable_events=True, key='liquid', font=("Arial", 15))],
        [sg.Text("Select interaction type", font=("Arial", 15))],
        [sg.Combo(neutron_interaction_options(), key='-INTERACTIONSINPUT-', font=("Arial", 15))],
        [sg.Text("Enter density", key='-FIRSTPARAM-', font=("Arial", 15))],
        [sg.Input(key='-FIRSTPARAMINPUT-', font=("Arial", 15))],
        [sg.Text("Enter molar mass of substance", key='-SECONDPARAM-', font=("Arial", 15))],
        [sg.Input(key='-SECONDPARAMINPUT-', font=("Arial", 15))],
        [sg.Text(size=(40, 1), key='-OUTPUT-', font=("Arial", 15))],
        [sg.Button('Compute', font=("Arial", 15))]
    ]
    window = sg.Window("Modelling", layout, size=(600, 400))
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'solid':
            window['-FIRSTPARAM-'].update("Enter density")
            window['-SECONDPARAM-'].update("Enter molar mass")
            continue
        if event == 'gas':
            window['-FIRSTPARAM-'].update('Enter pressure')
            window['-SECONDPARAM-'].update("Enter temperature")
            continue
        if event == 'liquid':
            window['-FIRSTPARAM-'].update("Enter density")
            window['-SECONDPARAM-'].update("Enter molar mass")
            continue

        if values["gas"] == 'true':
            window['-OUTPUT-'].update(
                str(length(
                    values['-INTERACTIONSINPUT-'],
                    amount_of_gas(float(values['-FIRSTPARAMINPUT-']), float(values['-SECONDPARAMINPUT-'])))
                )
                + " centimeters"
            )
        else:
            window['-OUTPUT-'].update(
                str(length(
                    values['-INTERACTIONSINPUT-'],
                    amount_of_gas(float(values['-FIRSTPARAMINPUT-']), float(values['-SECONDPARAMINPUT-'])))
                )
                + " centimeters"
            )
    window.close()
import PySimpleGUI as sg
from calculations import *


def neutron_interaction_options():
    return list(delta_map.keys())


if __name__ == "__main__":
    layout = [
        [sg.Text("Select state of aggregation", font=("Arial", 14))],
        [sg.Radio("solid", "SOARADIO", enable_events=True, default=True, key='solid', font=("Arial", 14))],
        [sg.Radio("gas", "SOARADIO", enable_events=True, key='gas', font=("Arial", 14))],
        [sg.Radio("liquid", "SOARADIO", enable_events=True, key='liquid', font=("Arial", 14))],
        [sg.Text("Select interaction type", font=("Arial", 14))],
        [sg.Combo(neutron_interaction_options(), key='-INTERACTIONSINPUT-', font=("Arial", 14))],
        [sg.Text("Formula", key='-FORMULA-', font=("Arial", 14))],
        [sg.Input(key='-FORMULAINPUT-', font=("Arial", 14))],
        [sg.Text("p", key='-FIRSTPARAM-', font=("Arial", 14))],
        [sg.Input(key='-FIRSTPARAMINPUT-', font=("Arial", 14))],
        [sg.Text("", key='-SECONDPARAM-', font=("Arial", 14))],
        [sg.Input(key='-SECONDPARAMINPUT-', font=("Arial", 14))],
        [sg.Text(size=(40, 1), key='-OUTPUT-', font=("Arial", 14))],
        [sg.Button('Compute', font=("Arial", 14))]
    ]
    window = sg.Window("Modelling", layout, size=(600, 400))
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'solid':
            window['-FIRSTPARAM-'].update("p")
            window['-SECONDPARAM-'].update("")
            continue
        if event == 'gas':
            window['-FIRSTPARAM-'].update('P')
            window['-SECONDPARAM-'].update("T")
            continue
        if event == 'liquid':
            window['-FIRSTPARAM-'].update("p")
            window['-SECONDPARAM-'].update("")
            continue

        if values["gas"] == 'true':
            window['-OUTPUT-'].update(
                str(length(
                    values['-INTERACTIONSINPUT-'],
                    amount_of_gas(
                        float(values['-FIRSTPARAMINPUT-']),
                        float(values['-SECONDPARAMINPUT-'])) * sum(parse_amount_of_atoms(values['-FORMULAINPUT-'])))
                )
                + " centimeters"
            )
        else:
            window['-OUTPUT-'].update(
                str(length(
                    values['-INTERACTIONSINPUT-'],
                    amount_of_solid(
                        float(values['-FIRSTPARAMINPUT-']),
                        parse_molar_mass(values['-FORMULAINPUT-'])
                    ) * sum(parse_amount_of_atoms(values['-FORMULAINPUT-']).values())))
                + " centimeters"
            )
    window.close()

from converter14 import convert
import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet")
input1 =sg.Input(key="feet")
label2 = sg.Text("Enter inches")
input2 =sg.Input(key="inches")
convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")
exit_button =sg.Button("Exit")


window = sg.Window("Convertor", layout=[
                                            [label1,input1],
                                            [label2, input2],
                                            [convert_button, exit_button, output_label]])


while True:
    event,values = window.read()
    print(event,values)
    if event == "Convert":
        try:
            converted_value = convert(float(values["feet"]),float(values["inches"]))
            window["output"].update(value=f"{converted_value} m")
        except ValueError:
            sg.popup("Please provide two numbers")

    if event == "Exit":
        exit()

    if event == sg.WIN_CLOSED:
        break

window.close()
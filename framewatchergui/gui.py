import PySimpleGUI as sg


def initGUI():

    layout = [
        [
            sg.Text("Watch Directory:", font=("Arial 16")),
            sg.InputText(font=("Arial 16")),
            sg.FileBrowse(font=("Arial 12")),
        ],
        [
            sg.Text("Processed Directory:", font=("Arial 16")),
            sg.InputText(font=("Arial 16")),
            sg.FileBrowse(font=("Arial 12")),
        ],
        [sg.Checkbox("Align", default=True, font=("Arial 16"))],
        [
            sg.Frame(
                title="Align Options",
                font=("Arial 12"),
                layout=[
                    [
                        sg.Text("Output Directory:", font=("Arial 12")),
                        sg.InputText(font=("Arial 12")),
                        sg.FileBrowse(font=("Arial 12")),
                    ],
                    [
                        sg.Text("binning", font=("Arial 12")),
                        sg.InputText(font=("Arial 12")),
                    ],
                    [
                        sg.Text("power", font=("Arial 12")),
                        sg.InputText(font=("Arial 12")),
                    ],
                    [
                        sg.Text("thumb directory", font=("Arial 12")),
                        sg.InputText(font=("Arial 12")),
                        sg.FileBrowse(font=("Arial 12")),
                    ],
                    [
                        sg.Text("dtotal", font=("Arial 12")),
                        sg.InputText(font=("Arial 12")),
                    ],
                    [
                        sg.Text("volt", font=("Arial 12")),
                        sg.InputText(font=("Arial 12")),
                    ],
                    [sg.Text("", font=("Arial 12"))],
                    [sg.Text("Workers", font=("Arial 16"))],
                    [
                        sg.Text("GPU", font=("Arial 12")),
                        sg.InputText("-1", size=(5, 1), font=("Arial 12")),
                    ],
                    [
                        sg.Text("# of threads", font=("Arial 12")),
                        sg.InputText("5", size=(5, 1), font=("Arial 12")),
                    ],
                    [
                        sg.Text("GPU", font=("Arial 12")),
                        sg.InputText("-1", size=(5, 1), font=("Arial 12")),
                    ],
                    [
                        sg.Text("# of threads", font=("Arial 12")),
                        sg.InputText("5", size=(5, 1), font=("Arial 12")),
                    ],
                    [
                        sg.Text("GPU", font=("Arial 12")),
                        sg.InputText("-1", size=(5, 1), font=("Arial 12")),
                    ],
                    [
                        sg.Text("# of threads", font=("Arial 12")),
                        sg.InputText("5", size=(5, 1), font=("Arial 12")),
                    ],
                ],
            )
        ],
        [
            sg.Button("Start", font=("Arial 16"), key="Start"),
            sg.Button("Stop", font=("Arial 16"), key="Stop"),
            sg.Button("Close", font=("Arial 16"), key="Close"),
        ],
        [
            sg.Multiline(size=(50, 10), font=("Arial 16"), key="shipper_log"),
            sg.Multiline(size=(50, 10), font=("Arial 16"), key="worker1_log"),
            sg.Multiline(size=(50, 10), font=("Arial 16")),
        ],
    ]

    window = sg.Window("Framewatcher GUI", layout)
    window.Finalize()
    window.Element('Stop').Update(disabled=True)
    return window


if __name__ == "__main__":
    window = initGUI()
    event, values = window.Read()

    print(event)
    print(values)

    window.Close()

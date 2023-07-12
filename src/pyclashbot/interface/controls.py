import PySimpleGUI as sg

from pyclashbot.interface.theme import THEME

sg.theme(THEME)


controls = [
    [
        sg.Button("Start", expand_x=True),
        sg.Button("Stop", disabled=True, expand_x=True),
        sg.Button("Pause", disabled=True, key="-Pause-Resume-Button-", expand_x=True),
    ],
    [
        sg.P(),
        sg.Text(
            "# of Accounts: ",
        ),
        sg.Combo(
            ["1", "2", "3", "4"],
            key="-SSID_IN-",
            default_value="1",
            enable_events=True,
        ),
        sg.P(),
    ],
    [sg.VP()],
    [sg.HSep(color="lightgray")],
    [
        sg.Button("Discord", key="discord", expand_x=True),
        sg.Button("Report Bug", key="bug-report", expand_x=True),
    ],
]

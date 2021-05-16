"""
Password Generator
"""
import secrets
import PySimpleGUI as sg
from tkinter import Tk

# Symbols allowed
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "1234567890"
symb = "!£$%&/()=?^'"
total = lower + upper + num + symb
stringa = ""

# Layout and Window Setup
layout = [[sg.Text("Quanto vuoi che sia lunga la tua password?", text_color="black")], [sg.InputText(key="length",
                                                                                                     size=(3, 1))],
          [sg.Button("Genera")], [sg.Text("", size=(20, 2), key="hereitis")], [sg.Text("", size=(20, 1), key="password",
                                                                                       text_color="black")],
          [sg.Button("Copia")], [sg.Text("", key="copied", size=(6, 1), text_color="black")]]
window = sg.Window("Password Generator", layout, font="Roboto", element_justification="center")

# Clipboard Setup
r = Tk()
r.withdraw()
r.clipboard_clear()

while True:
    event, values = window.read()
    # Generating the password
    if event == "Genera":
        stringa = ""
        # First error handler
        if len(values["length"]) == 0:
            window.Element("hereitis").update("Hai dimenticato di mettere un numero!", text_color="red")
        else:
            # Second error handler
            if values["length"] == "0":
                window.Element("hereitis").update("La password non può avere 0 caratteri!", text_color="red")
            else:
                length = int(values["length"])
                for i in range(0, length):
                    rand = secrets.randbelow(len(total))
                    stringa += total[rand]
                window.Element("hereitis").update("Ecco la tua nuova password!", text_color="black")
        window.Element("password").update(stringa)
    # Copying the password to clipboard
    if event == "Copia":
        r.clipboard_append(stringa)
        r.update()
        window.Element("copied").update("Copiato")
    # Closing the window
    if event == sg.WIN_CLOSED:
        break
window.close()

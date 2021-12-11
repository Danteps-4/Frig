import tkinter as tk
import webbrowser
from tkinter import ttk, scrolledtext
from Frig.widgets.Colors import Colors


class Instructions:
    def __init__(self, master):
        self._master = master

        #Create the frame
        self._instructions_frame = ttk.Frame(self._master)
        #Config the frame
        self._instructions_frame.columnconfigure(0, weight=1)
        self._instructions_frame.rowconfigure(0, weight=10)
        self._instructions_frame.rowconfigure(1, weight=1)
        #Add the frame to the master
        self._master.add(self._instructions_frame, text="Instructions")

    def instructions_components(self):
        # ScrolledText for the instructions.txt
        instructions_text = scrolledtext.ScrolledText(self._instructions_frame, wrap=tk.WORD)
        instructions_text.grid(row=0, column=0, sticky="NSWE")
        # Adding instructions.txt to instructions_text
        self.open_file("Frames/Instructions/instructions.txt", instructions_text)

        # Label for the link to the instructions website
        instructions_button = tk.Label(self._instructions_frame, text="Visit the instructions website", fg=Colors.BLUE, cursor="hand2")
        instructions_button.grid(row=1, column=0)
        instructions_button.bind("<Button-1>", lambda e:
        self.callback("http://www.tutorialspoint.com"))

    def open_file(self, address, entry):
        with open(address, "r") as file:
            text = file.read()
            entry.insert(tk.INSERT, text)

    def callback(self, url):
        webbrowser.open_new_tab(url)
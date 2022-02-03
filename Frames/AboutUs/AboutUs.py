import webbrowser
from tkinter import ttk
import tkinter as tk
from Frig.widgets.Colors import Colors

class AboutUs:
    def __init__(self, master):
        self._master = master

        #Create the frame
        self._about_us_frame = ttk.Frame(self._master)

        #Add the frame to the master
        self._master.add(self._about_us_frame, text="About us")

    def about_us_components(self):
        # Frig
        title = ttk.Label(self._about_us_frame, text="Frig", font=("Arial", 35))
        title.pack()
        subtitle = ttk.Label(self._about_us_frame, text="Try your luck", font=("Arial", 22))
        subtitle.pack()

        # What is frig?
        what_frig_label = ttk.Label(self._about_us_frame, text="What is Frig?", font=("Arial", 18))
        what_frig_label.pack(pady=(30, 10))
        what_frig_description = ttk.Label(self._about_us_frame, text="Frig is a project with the objective of evaluating the luck of the users through a rock, paper or scissors game. Users have 1 of 3 possibilities of win, lose or draw but we are going to center our atention on the wins. Frig is going to track your stats and it will display how lucky you are.", font=("Arial", 12), wraplength=700, justify=tk.CENTER)
        what_frig_description.pack()

        # Who we are?
        who_are_label = ttk.Label(self._about_us_frame, text="Who we are?", font=("Arial", 18))
        who_are_label.pack(pady=(30, 10))
        who_are_description = ttk.Label(self._about_us_frame, text="Our team is composed by Dante Augsburger and Santos Zuberbuhler, two friends that joined to make this project together :D", font=("Arial", 12), wraplength=700, justify=tk.CENTER)
        who_are_description.pack()

        visit_website_label = tk.Label(self._about_us_frame, text="Visit the website", fg=Colors.BLUE, cursor="hand2", font=("Arial", 12))
        visit_website_label.pack(pady=20)
        visit_website_label.bind("<Button-1>", lambda e:
        self._callback("https://santoszuber.github.io/Frig/index.html"))


        self._creators_stuff_frame()

    def _creators_stuff_frame(self):
        creators_frame = tk.Frame(self._about_us_frame)
        creators_frame.columnconfigure(0, minsize=300, weight=1)
        creators_frame.columnconfigure(1, minsize=300, weight=5)
        creators_frame.pack(pady=(40, 0))

        # Dante Augsburger
        dante_stuff = tk.Label(creators_frame, text="Dante Augsburger:", font=("Arial", 12))
        dante_stuff.grid(row=0, column=0)
        dante_github = tk.Label(creators_frame, text="Github", cursor="hand2", fg=Colors.BLUE, font=("Arial", 12))
        dante_github.grid(row=1, column=0)
        dante_github.bind("<Button-1>", lambda e:
        self._callback("https://github.com/Danteps-4"))

        # Santos Zuberbuhler
        santos_stuff = tk.Label(creators_frame, text="Santos Zuberbuhler:", font=("Arial", 12))
        santos_stuff.grid(row=0, column=1)
        santos_github = tk.Label(creators_frame, text="Github", cursor="hand2", fg=Colors.BLUE, font=("Arial", 12))
        santos_github.grid(row=1, column=1)
        santos_github.bind("<Button-1>", lambda e:
        self._callback("https://github.com/SantosZuber"))

    def _callback(self, url):
        webbrowser.open_new_tab(url)
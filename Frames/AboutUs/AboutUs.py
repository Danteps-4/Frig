from tkinter import ttk

class AboutUs:
    def __init__(self, master):
        self._master = master

        #Create the frame
        self._about_us_frame = ttk.Frame(self._master)

        #Add the frame to the master
        self._master.add(self._about_us_frame, text="About us")

    def about_us_components(self):
        pass
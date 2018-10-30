# source/gui/gui.py

from tkinter import *
from tkinter import ttk


class Tab:
    """
    Hopefully handles low level tasks that accompany using frames and tabs with Tkinter.
    """

    def __init__(self, tab_control):
        self.tab = ttk.Frame(tab_control)


class Log(Tab):
    """
    One of the main tabs for the gui. Handles widgets involved with adding, altering, querying, and deleting
    data entries from the database.
    """
    def __init__(self, tab_control):
        Tab.__init__(self, tab_control=tab_control)
        header = Label(self.tab, text="Become a warrior!", font=("Franklin Gothic", 22))
        header.grid(column=0, row=0)

        data = ['Date', 'Distance', 'Time']
        data_text = ['Date (MM-DD-YYYY)', 'Distance (miles)', 'Time (hour:min:sec)']
        current_row = 1

        data_entries = {}
        data_labels = {}

        for i in range(len(data)):
            d_lbl = Label(self.tab, text=data_text[i])
            d_lbl.grid(column=0, row=current_row)
            data_labels[data[i]] = d_lbl
            current_row += 1
            d_entry = Entry(self.tab, width=15)
            d_entry.grid(column=0, row=current_row)
            data_entries[data[i]] = d_entry
            current_row += 1

        def add_entry():
            user_date = data_entries['Date'].get()
            data_entries['Date'].delete(0, len(user_date))
            user_dist = data_entries['Distance'].get()
            data_entries['Distance'].delete(0, len(user_dist))
            user_time = data_entries['Time'].get()
            data_entries['Time'].delete(0, len(user_time))
            print(user_date)
            print(user_dist)
            print(user_time)

        btn_add_entry = Button(self.tab, text="Add Entry", command=add_entry)
        btn_add_entry.grid(column=0, row=current_row)


class Stats(Tab):
    """
    One of the main tabs for the gui. Handles displaying statistical information for user to judge.
    """
    def __init__(self, tab_control):
        Tab.__init__(self, tab_control=tab_control)
        header = Label(self.tab, text="Lot's of stats!", font=("Franklin Gothic", 22))
        header.grid(column=0, row=0)


class Goals(Tab):
    """
    One of the main tabs for the gui. Handles writing and displaying for user goals to track progress.
    """
    def __init__(self, tab_control):
        Tab.__init__(self, tab_control=tab_control)
        header = Label(self.tab, text="What are your goals?", font=("Franklin Gothic", 22))
        header.grid(column=0, row=0)


class GUIManager:
    """
    API for Tkinter gui package for better organization of a dynamically changing gui.
    """

    def __init__(self):
        self.window = Tk()
        self.window.title("Fitness App")
        self.tab_control = ttk.Notebook(self.window)
        self.tabs = {}
        self.add_tabs()

    def add_tabs(self):
        self.tabs["Log"] = Log(self.tab_control)
        self.tab_control.add(self.tabs["Log"].tab, text="Log")
        self.tabs["Stats"] = Stats(self.tab_control)
        self.tab_control.add(self.tabs["Stats"].tab, text="Stats")
        self.tabs["Goals"] = Goals(self.tab_control)
        self.tab_control.add(self.tabs["Goals"].tab, text="Goals")
        self.tab_control.pack(expand=1, fill='both')

    def main_loop(self):
        self.window.mainloop()


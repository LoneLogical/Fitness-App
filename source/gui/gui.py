# source/gui/gui.py

from tkinter import *
# import datetime as dt

window = Tk()
window.title("Fitness App")
window.geometry('450x200')

header = Label(window, text="Become a warrior!", font=("Franklin Gothic", 25))
header.grid(column=0, row=0)

data = ['Date', 'Distance', 'Time']
data_text = ['Date (MM-DD-YYYY)', 'Distance (miles)', 'Time (hour:min:sec)']
current_row = 1

data_entries = {}
data_labels = {}

for i in range(len(data)):
    d_lbl = Label(window, text=data_text[i])
    d_lbl.grid(column=0, row=current_row)
    data_labels[data[i]] = d_lbl
    current_row += 1
    d_entry = Entry(window, width=15)
    d_entry.grid(column=0, row=current_row)
    data_entries[data[i]] = d_entry
    current_row += 1


def add_entry():
    user_date = data_entries['Date'].get()
    user_dist = data_entries['Distance'].get()
    user_time = data_entries['Time'].get()
    print(user_date)
    print(user_dist)
    print(user_time)


btn_add_entry = Button(window, text="Add Entry", command=add_entry)
btn_add_entry.grid(column=0, row=current_row)

window.mainloop()

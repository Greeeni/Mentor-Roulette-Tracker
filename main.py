import tkinter  as tk
from tkinter import ttk
import pandas as pd
from os.path import exists

def convert():
    print('Button has been clicked, convert')
    print(entry_int.get())
    output_string.set(entry_int.get())


if __name__ == "__main__":
    if exists("mentorroulette.csv"):
        print("CSV Exists, continuing")
    else:
        print("Generating CSV:")
        f = open("mentorroulette.csv", "xt")
        f.write("#,Date,Completed,Instance,Expansion,Category,Class,Party in Progress\n")
        f.close()




    window = tk.Tk()

    # Window
    window.title("demo")
    window.geometry("300x150")


    # Title
    title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 24 bold')
    title_label.pack()


    # Input Field
    input_frame = ttk.Frame(master = window)
    entry_int = tk.IntVar()
    entry = ttk.Entry(master = input_frame, textvariable = entry_int)
    button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
    entry.pack(side = 'left', padx = 10)
    button.pack(side = 'left')
    input_frame.pack(pady = 10)

    # Output
    output_string = tk.StringVar()
    output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24', textvariable = output_string)
    output_label.pack(pady = 5)

    # Run
    window.mainloop()
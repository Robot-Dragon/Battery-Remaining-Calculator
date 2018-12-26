import tkinter as tk
from tkinter import END
from tkinter import ttk
import datetime
from datetime import timedelta

class BatteryCalculator:
    # Initialize window and all frames and contained widgets
    def __init__(self, master):
        self.master = master
        master.title("nbn Battery Calculator")
        master.resizable(width=False, height=False)
        master.geometry("400x170")

        # The below creates a frame for labels
        labelframe = tk.Frame()
        labelframe.grid(column=0, row=0, sticky=tk.W)

        self.label1 = tk.Label(labelframe,
            text="Enter the current battery capacity (in Ah):")
        self.label1.grid(column=0, row=0, sticky=tk.W)

        self.label2 = tk.Label(labelframe,
            text="Enter the current capacity discharged (in Ah):")
        self.label2.grid(column=0, row=1, sticky=tk.W)

        self.label3 = tk.Label(labelframe,
            text="Enter the battery current (in A):")
        self.label3.grid(column=0, row=2, sticky=tk.W)

        # The below creates the frame for the text entry fields
        inputframe = tk.Frame()
        inputframe.grid(column=1, row=0, sticky=tk.E)

        self.entry1 = ttk.Entry(inputframe)
        self.entry1.grid(column=0, row=0, sticky=tk.W)
        self.entry1.bind('<Return>', self.calculate_remaining)

        self.entry2 = ttk.Entry(inputframe)
        self.entry2.grid(column=0, row=1, sticky=tk.W)
        self.entry2.bind('<Return>', self.calculate_remaining)

        self.entry3 = ttk.Entry(inputframe)
        self.entry3.grid(column=0, row=2, sticky=tk.W)
        self.entry3.bind('<Return>', self.calculate_remaining)

        # The below frame is for output display
        outputframe = tk.Frame()
        outputframe.grid(column=0, row=1, columnspan=2, sticky=tk.W)

        self.remainingtime = tk.Label(outputframe,
            text="Battery will expire in (hh:mm):")
        self.remainingtime.grid(column=0, row=0, sticky=tk.W)

        self.currenttime = tk.Label(outputframe,
            text="The current date/time is:")
        self.currenttime.grid(column=0, row=1, sticky=tk.W)

        self.expirytime = tk.Label(outputframe,
            text="Predicted battery expiry date/time is:")
        self.expirytime.grid(column=0, row=2, sticky=tk.W)

        # The below creates and manages the button frame
        buttonframe = tk.Frame()
        buttonframe.grid(column=1, row=2, sticky=tk.E)

        self.button1 = ttk.Button(buttonframe,
            text="Calculate", command=self.calculate_remaining)
        self.button1.grid(column=0, row=0)

        self.button2 = ttk.Button(buttonframe,
            text="Reset", command=self.reset_all)
        self.button2.grid(column=1, row=0)

    # The function to calculate result of the 3 inputs from user entry fields
    # The function will also update labels text with results
    def calculate_remaining(self, *args, **kwargs):
        bat_cap = float(self.entry1.get())
        cur_cap_dis = float(self.entry2.get())
        bat_cur = float(self.entry3.get())
        env_var = 0.7

        result = (((bat_cap - cur_cap_dis) / bat_cur) * env_var)
        hours = int(result)
        minutes = (result*60) % 60

        now = datetime.datetime.now()
        expiry_time = (now +
            datetime.timedelta(hours = hours, minutes = minutes))

        self.remainingtime["text"] = ("Battery will expire in (hh:mm): " +
            "%d:%02d" % (hours, minutes))
        self.currenttime["text"] = ("The current date/time is: " +
            now.strftime("%Y-%m-%d %H:%M"))
        self.expirytime["text"] = ("Predicted battery expiry date/time is: " +
            expiry_time.strftime("%Y-%m-%d %H:%M"))

    # Function to clear all input fields
    def reset_all(self, *args, **kwargs):
        self.remainingtime["text"] = ("Battery will expire in:")
        self.currenttime["text"] = ("The current date/time is:")
        self.expirytime["text"] = ("Predicted battery expiry date/time is:")

        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)


root = tk.Tk()
myapp = BatteryCalculator(root)
root.mainloop()

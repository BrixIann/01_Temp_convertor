from tkinter import *
from functools import partial  # To prevent unwanted windows
import random

class Start:
    def __init__(self, parent):

        #GUI to get tarting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        #Mystery Heading (row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game", font="Arial 19 bold")
        self.mystery_box_label.grid(row=1)

        #Entry box... (row 1)
        self.start_amount_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_amount_entry.grid(row=2)
        
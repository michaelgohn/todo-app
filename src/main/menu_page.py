import tkinter as tk
import ttkbootstrap as ttk

class Menu_Page(ttk.Frame):
    
    def __init__(self, master, borderwidth=None, relief=None):
        super().__init__(master=master, borderwidth=borderwidth, relief=relief)
        # self.pack(fill='both', expand=True)
        frame_1 = ttk.Frame(master=self, padding=30)
        frame_2 = ttk.Frame(master=self, padding=30)
        frame_3 = ttk.Frame(master=self, padding=30)
        ttk.Label(master=frame_1, text='Hello User!', font=('Calibri', 17)).pack()
        ttk.Label(master=frame_2, text='Welcome to your To Do App!', font=('Calibri', 17)).pack()
        ttk.Button(master=frame_3, text='View To Do List').pack()
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        self.pack(fill='both', expand=True)
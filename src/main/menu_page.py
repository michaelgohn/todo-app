import tkinter as tk
import ttkbootstrap as ttk

class Menu_Page(ttk.Frame):
    
    def __init__(self, master, frames=None, borderwidth=None, relief=None):

        # Create menu page object
        super().__init__(master=master, borderwidth=borderwidth, relief=relief)
        self.frames = frames

        # Create children frames
        frame_1 = ttk.Frame(master=self, padding=30)
        frame_2 = ttk.Frame(master=self, padding=30)
        frame_3 = ttk.Frame(master=self, padding=30)

        # Create children widgets
        ttk.Label(master=frame_1, text='Hello User!', font=('Calibri', 17)).pack()
        ttk.Label(master=frame_2, text='Welcome to your To Do App!', font=('Calibri', 17)).pack()
        ttk.Button(master=frame_3, text='View To Do List', command=lambda: self.show_page('todo_list_page')).pack()

        # Pack everything
        frame_1.pack()
        frame_2.pack()
        frame_3.pack()
        self.pack(fill='both', expand=True)

    def set_frames(self, frames):
        self.frames = frames

    """
    Allows you to view the To Do List page.

    Parameters:
    page_name (string): String key for frames dictionary

    Returns:
    void: Displays To Do List
    """
    def show_page(self, page_name):
        self.pack_forget()
        self.frames[page_name].pack(fill='both', expand=True)
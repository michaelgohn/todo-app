import tkinter as tk
import ttkbootstrap as ttk

class Edit_Todo_Page(ttk.Frame):

    def __init__(self, master, frames=None, borderwidth=None, relief=None):
        """
        Allows you to view the To Do List page.

        Parameters:
        page_name (string): String key for frames dictionary

        Returns:
        void: Displays To Do List
        """
        def show_page(page_name):
            self.pack_forget()
            self.frames[page_name].pack(fill='both', expand=True)

        super().__init__(master=master, borderwidth=borderwidth, relief=relief)
        self.frames = frames

    def set_frames(self, frames):
        self.frames = frames
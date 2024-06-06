import tkinter as tk
import ttkbootstrap as ttk

class Todo_List_Page(ttk.Frame):

    def __init__(self, master, test_item_list, frames=None, borderwidth=None, relief=None):

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
        self.test_item_list = test_item_list

        for todo_item in test_item_list:
            frame = ttk.Frame(master=self, borderwidth=10, relief='groove', padding='100 20')
            ttk.Label(master=frame, text=todo_item.desc).pack()
            frame.pack(pady=10)
        # ttk.Label(master=self, text='Hello loyal viewers!', font=('Calibri', 17)).pack()

    def set_frames(self, frames):
        self.frames = frames
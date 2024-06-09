import tkinter as tk
import ttkbootstrap as ttk
from todo_item import Todo_Item
from tkinter import messagebox

class Add_Todo_Page(ttk.Frame):

    def __init__(self, master, todo_item_list, frames=None, borderwidth=None, relief=None):

        super().__init__(master=master, borderwidth=borderwidth, relief=relief)
        self.frames = frames
        self.item_desc = tk.StringVar(value='Item Description')
        self.item_to_add = None
        self.todo_item_list = todo_item_list

        top_frame = ttk.Frame(master=self, padding='20 50')
        bottom_frame = ttk.Frame(master=self, padding='20 50')

        ttk.Entry(master=top_frame, width=30, font='Calibri 17', textvariable=self.item_desc).pack()
        ttk.Button(master=bottom_frame, width=30, text='Add', command=self.add_todo_item).pack(side='left', padx=10)
        ttk.Button(master=bottom_frame, width=30, text='Cancel', command=lambda: self.show_page('todo_list_page')).pack(side='right', padx=10)

        top_frame.pack()
        bottom_frame.pack()

    def set_frames(self, frames):
        self.frames = frames

    """
    Creates todo item and adds it to todo item list. Then shows todo_list_page.

    Parameters:
    N/A

    Returns:
    void
    """
    def add_todo_item(self):
        if not self.item_desc.get() or self.item_desc.get() == 'Item Description':
            print(self.todo_item_list)
            messagebox.showerror(title='Error', message='Item description cannot be empty or default value')
            print(self.todo_item_list)
        else:
            print(self.todo_item_list)
            todo_item = Todo_Item(desc=tk.StringVar(value=self.item_desc.get()), is_checked=tk.BooleanVar(value=False))
            self.todo_item_list.append(todo_item)
            self.frames['todo_list_page'].create_item(todo_item)
            self.show_page('todo_list_page')
            print(self.todo_item_list)

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
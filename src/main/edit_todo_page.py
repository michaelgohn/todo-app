import tkinter as tk
import ttkbootstrap as ttk

class Edit_Todo_Page(ttk.Frame):

    def __init__(self, master, frames=None, borderwidth=None, relief=None):

        super().__init__(master=master, borderwidth=borderwidth, relief=relief)
        self.frames = frames
        self.item_desc = tk.StringVar(value='Item Description')
        self.item_to_edit = None

        top_frame = ttk.Frame(master=self, padding='20 50')
        bottom_frame = ttk.Frame(master=self, padding='20 50')

        ttk.Entry(master=top_frame, width=30, font='Calibri 17', textvariable=self.item_desc).pack()
        ttk.Button(master=bottom_frame, width=30, text='Save', command=lambda: self.save_desc(self.item_desc)).pack(side='left', padx=10)
        ttk.Button(master=bottom_frame, width=30, text='Cancel', command=lambda: self.show_page('todo_list_page')).pack(side='right', padx=10)

        top_frame.pack()
        bottom_frame.pack()

    def set_frames(self, frames):
        self.frames = frames

    """
    Saves the new description of the todo item

    Parameters:
    new_desc (tk.StringVar): tkinter String variable to track entry input

    Returns:
    void: Saves todo item's new description
    """
    def save_desc(self, new_desc):
        self.item_to_edit.desc.set(new_desc.get())
        self.show_page('todo_list_page')

    """
    Prepares necessary variables on edit todo page

    Parameters:
    todo_item (Todo_Item): Item to be edited

    Returns:
    void: Preps variables
    """
    def prepare_edit_page(self, todo_item):
        self.frames['todo_list_page'].show_page('edit_todo_page')
        self.item_to_edit = todo_item
        self.item_desc.set(todo_item.desc.get())

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
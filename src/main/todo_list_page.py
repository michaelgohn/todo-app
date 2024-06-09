import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk

class Todo_List_Page(ttk.Frame):

    def __init__(self, master, todo_item_list, frames=None, borderwidth=None, relief=None):

        super().__init__(master=master, borderwidth=borderwidth, relief=relief)
        self.frames = frames
        self.todo_item_list = todo_item_list
        self.image_refs = []
        self.page_container = ttk.Frame(master=self)

        # Icon loadings
        pencil_image_path = 'C:\\Users\\gabe\\Documents\\my-vscode\\projects\\todo-app\\src\\icons\\pencil-icon.png'
        self.pencil_icon = self.load_image(pencil_image_path)
        x_image_path = 'C:\\Users\\gabe\\Documents\\my-vscode\\projects\\todo-app\\src\\icons\\x-icon.png'
        self.x_icon = self.load_image(x_image_path)

        # Create todo item frames
        for todo_item in todo_item_list:
            frame = ttk.Frame(master=self.page_container, borderwidth=10, relief='groove', padding='100 20')

            ttk.Checkbutton(master=frame, variable=todo_item.is_checked).pack(side='left', padx=5)
            ttk.Label(master=frame, text=todo_item.desc, textvariable=todo_item.desc).pack(side='left', padx=20)
            ttk.Button(master=frame, image=self.x_icon, command=lambda item=todo_item: self.delete_todo_item(item)).pack(side='right', padx=5)
            ttk.Button(master=frame, image=self.pencil_icon, command=lambda item=todo_item: self.frames['edit_todo_page'].prepare_edit_page(item)).pack(side='right', padx=5)
            frame.pack(pady=10)
            todo_item.set_item_frame(frame)
        
        self.page_container.pack(fill='both', expand=True)

        # Bottom main menu button
        bottom_frame = ttk.Frame(master=self)
        ttk.Button(master=bottom_frame, text='Add', command=lambda: self.show_page('add_todo_page')).pack(side='left', padx=10)
        ttk.Button(master=bottom_frame, text='Main Menu', command=lambda: self.show_page('menu_page')).pack(side='right', padx=10)
        bottom_frame.pack(side='bottom', pady=10)

    def set_frames(self, frames):
        self.frames = frames

    """
    Creates todo item interface and adds it to parent frame

    Parameters:
    todo_item (Todo_Item): todo_item to have interface created

    Returns:
    void
    """
    def create_item(self, todo_item):
        frame = ttk.Frame(master=self.page_container, borderwidth=10, relief='groove', padding='100 20')

        ttk.Checkbutton(master=frame, variable=todo_item.is_checked).pack(side='left', padx=5)
        ttk.Label(master=frame, text=todo_item.desc, textvariable=todo_item.desc).pack(side='left', padx=20)
        ttk.Button(master=frame, image=self.x_icon, command=lambda item=todo_item: self.delete_todo_item(item)).pack(side='right', padx=5)
        ttk.Button(master=frame, image=self.pencil_icon, command=lambda item=todo_item: self.frames['edit_todo_page'].prepare_edit_page(item)).pack(side='right', padx=5)
        frame.pack(pady=10)
        todo_item.set_item_frame(frame)

    """
    Allows user to delete todo item

    Parameters:
    todo_item (Todo_Item): Item to be deleted

    Returns:
    void: Deletes todo item
    """
    def delete_todo_item(self, todo_item):
        todo_item.get_item_frame().forget()
        self.todo_item_list.remove(todo_item)

    """
    Allows user to view the To Do List page.

    Parameters:
    page_name (string): String key for frames dictionary

    Returns:
    void: Displays To Do List
    """
    def show_page(self, page_name):
        self.pack_forget()
        self.frames[page_name].pack(fill='both', expand=True)

    """
    Loads images

    Parameters:
    image_path (string): String to store image path

    Returns:
    PhotoImage: Object storing image
    """
    def load_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize((15, 15))
        icon = ImageTk.PhotoImage(image)
        self.image_refs.append(icon)
        return icon
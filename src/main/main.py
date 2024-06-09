import tkinter as tk
import ttkbootstrap as ttk
from menu_page import Menu_Page
from todo_list_page import Todo_List_Page
from add_todo_page import Add_Todo_Page
from edit_todo_page import Edit_Todo_Page
from todo_item import Todo_Item

# Setup
window = ttk.Window(themename='litera')
window.title('To Do App')
window.geometry('600x350')
frames = {}
# Temp Data
todo_item_1 = Todo_Item(tk.StringVar(value='Test Todo Item 1'), tk.BooleanVar(value=False))
todo_item_2 = Todo_Item(tk.StringVar(value='Test Todo Item 2'), tk.BooleanVar(value=False))
todo_item_list = [todo_item_1, todo_item_2]

# Create Main Menu
add_todo_page = Add_Todo_Page(master=window, todo_item_list=todo_item_list)
edit_todo_page = Edit_Todo_Page(master=window)
todo_list_page = Todo_List_Page(master=window, todo_item_list=todo_item_list)
menu_page = Menu_Page(master=window)

# Populate frames dictionary
frames['add_todo_page'] = add_todo_page
frames['edit_todo_page'] = edit_todo_page
frames['todo_list_page'] = todo_list_page
frames['menu_page'] = menu_page

# Add frames dictionary to page widgets
add_todo_page.set_frames(frames=frames)
edit_todo_page.set_frames(frames=frames)
todo_list_page.set_frames(frames=frames)
menu_page.set_frames(frames=frames)

# Run
window.mainloop()
import tkinter as tk
import ttkbootstrap as ttk
from menu_page import Menu_Page

# Setup
window = ttk.Window(themename='litera')
window.title('To Do App')
window.geometry('600x350')

# Create Main Menu
main_page = Menu_Page(master=window)

# Run
window.mainloop()
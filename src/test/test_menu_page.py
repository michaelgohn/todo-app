import unittest
# from unittest.mock import patch
import sys
import os
import tkinter as tk
import ttkbootstrap as ttk

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'main'))
import main

class TestMenuPage(unittest.TestCase):

    # def test_init(self):
    #     with patch(tk.Tk) as test_window:
    #         # Test no borderwidth, relief
    #         obj = main.Menu_Page(master=test_window)
    #         self.assertIsInstance(obj, main.Menu_Page)
    pass

if __name__ == '__main__':
    unittest.main()
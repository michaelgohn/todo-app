from datetime import datetime as dt

class Todo_Item():

    def __init__(self, desc, is_checked):
        self.desc = desc
        self.is_checked = is_checked
        self.time_checked = dt.now()
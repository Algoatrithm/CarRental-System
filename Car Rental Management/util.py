from tkinter import ttk



class Utilities:
    def __init__(self):
        pass
    def setup(self, winx, winy):
        self.x_screen = winx
        self.y_screen = winy

        self.X_CENTER = self.x_screen/2
        self.X_RIGHT = self.x_screen
        self.X_LEFT = 0

        self.Y_CENTER = self.y_screen/2
        self.Y_UP = 0
        self.Y_DOWN = self.y_screen

    x_screen: int = 0
    y_screen: int = 0

    X_CENTER: int = x_screen/2
    X_RIGHT: int = x_screen
    X_LEFT: int = 0

    Y_CENTER: int = y_screen/2
    Y_UP: int = 0
    Y_DOWN: int = y_screen

    seperation: int = 0

    row_manager: int = 0
    column_manager: int = 0

    def Label(self, ttk: ttk, root, text: str = "Empty", X_POSITION: int = 0, Y_POSITION: int = 0):
        ttk.Label(root, text=text).grid(row=self.row_manager, column=self.column_manager, padx=X_POSITION, pady=Y_POSITION + self.seperation, sticky="e")
        self.row_manager += 1
    def Button(self, ttk: ttk, root, text: str = "Empty", X_POSITION: int = 0, Y_POSITION: int = 0):
        ttk.Button(root, text=text).grid(row=self.row_manager, column=self.column_manager, padx=X_POSITION, pady=Y_POSITION + self.seperation, sticky="e")
        self.row_manager += 1
    
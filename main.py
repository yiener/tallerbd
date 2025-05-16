import tkinter as tk
from controlador import Controlador

if __name__ == "__main__":
    root = tk.Tk()
    app = Controlador(root)
    root.mainloop()
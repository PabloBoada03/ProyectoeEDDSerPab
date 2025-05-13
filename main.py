from frontend.view import Vista
import tkinter as tk

def main():
    root = tk.Tk()
    app = Vista(root)
    root.mainloop()

if __name__ == "__main__":
    main()

from tkinter import Tk
from ui import UI

def main():
    window = Tk()
    window.title("Budgeting application")

    ui_view = UI(window)
    ui_view.start()

    window.mainloop()


if __name__ == "__main__":
    main()
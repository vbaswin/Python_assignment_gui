import tkinter as tk

class LabelDemo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Aswin's GUI")
        label = tk.Label(self, text="Aswin's GUI")
        label.pack()

def main():
    LabelDemo().mainloop()

if __name__ == "__main__":
    main()

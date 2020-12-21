from tkinter import *

class App():

    def __init__(self):
        
        self.root = Tk()
        self.root.title("YOUTUBE DOWNLOADER")
        self.root.geometry("1000x550")
        self.root.resizable(False, False)
        self.root.config(bg  = "#202020")

        self.frame_title = Frame(self.root)
        self.frame_title.pack(pady = 100)

        self.frame_entry = Frame(self.root, bg = "#404040")
        self.frame_entry.pack()

        self.frame_button = Frame(self.root)
        self.frame_button.pack(pady = 100)

        self.title = Label(self.frame_title, text="YouTube downlader", font=("Rockwell Extra Bold", 30, "bold"), bg = "#404040", fg = "#FF3333")
        self.title.pack()

        self.label_entry = Label(self.frame_entry, text = "YouTube link: ", font=("Arial", 15, "bold"), bg = "#404040", fg = "#FF3333")
        self.label_entry.grid(row = 0, column = 0)

        self.entry = Entry(self.frame_entry, font=("Arial", 15), width = 50, bg = "#808080", fg = "#FD3131")
        self.entry.grid(row = 0, column = 1)

        self.button = Button(self.frame_button, text = "Find", font=("Arial", 25), pady = 15, padx = 50, bg = "#404040", fg = "#FF3333", bd = 0, activebackground = "#404040", activeforeground = "#FF3333")

        self.button.pack()



        self.root.mainloop()

app = App()
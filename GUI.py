from tkinter import *

class App():

    def __init__(self):
        
        self.root = Tk()

        self.frame_title = Frame(self.root)
        self.frame_title.pack()

        self.frame_entry = Frame(self.root)
        self.frame_entry.pack()

        self.frame_button = Frame(self.root)
        self.frame_button.pack()

        self.title = Label(self.frame_title, text="YouTube downlader", font=("Rockwell Extra Bold", 30, "bold"))
        self.title.pack()

        self.label_entry = Label(self.frame_entry, text = "YouTube link: ", font=("Arial", 15, "bold"))
        self.label_entry.grid(row = 0, column = 0)

        self.entry = Entry(self.frame_entry, font=("Arial", 15), width = 40)
        self.entry.grid(row = 0, column = 1)

        self.button = Button(self.frame_button, text = "Find", font=("Arial", 15))
        self.button.pack()



        self.root.mainloop()

app = App()
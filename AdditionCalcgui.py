from Tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widget()

    def create_widget(self):
        self.lbl = Label(self, text="Enter two numbers: ")
        self.lbl.grid()
        self.ent = Entry(self, width=30)
        self.ent.grid()
        self.ent_2 = Entry(self, width=30)
        self.ent_2.grid()
        self.lbl_sum = Label(self, text="The sum:")
        self.lbl_sum.grid()
        self.bttn = Button(self)
        self.bttn["text"]= "Add Numbers"
        self.bttn["command"] = self.update_sum
        self.bttn.grid()

    def update_sum(self):
        try:
            self.lbl_sum["text"] = "The sum: " + str((int(self.ent.get()) + int(self.ent_2.get())))
        except:
            self.lbl_sum["text"] = "Error: invalid value."
        self.ent.delete(0, END)
        self.ent_2.delete(0,END) 

# main
root = Tk()
root.title("Simple Adder")
root.geometry("300x200")
root.resizable(width = TRUE, height = TRUE)

app = Application(root)
root.mainloop()

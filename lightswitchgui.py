from Tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.bttn = Button(self, text = "Light is: OFF", command = self.update_button)
        self.bttn.grid()
 
    def update_button(self):
        if self.bttn["text"] == "Light is: OFF":           
            self.bttn["text"] = "Light is: ON"
        else:
            self.bttn["text"] = "Light is: OFF"

# main
root = Tk()
root.title("Event Handler Demo")
root.geometry("250x75")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()

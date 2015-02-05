from Tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        self.lbl = Label(self, text="Click to increment!")
        self.lbl.grid()
        self.bttn = Button(self, text = "Total Clicks: 0",command = self.update_button)
        self.bttn.grid()

    def update_button(self):
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks) 
                           

    #define a method to serve as the event handler
    #the method should increment the attribute
    #and update the text for the button as well!

# main
root = Tk()
root.title("Click Counter")
root.geometry("200x50")
root.resizable(width = FALSE, height = FALSE)

app = Application(root)
root.mainloop()

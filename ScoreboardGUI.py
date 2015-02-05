from Tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.bttn_clicks = 0
        self.bttn_clicks_visitor = 3
        self.create_widgets()

    def create_widgets(self):
        self.lbl_home = Label(self, text="Home Team: "+ str(self.bttn_clicks))
        self.lbl_home.grid()
        self.lbl_visitor = Label(self, text="Visitors: "+ str(self.bttn_clicks_visitor))
        self.lbl_visitor.grid()
        self.lbl_winning = Label(self, text="Winning: Visitors")
        self.lbl_winning.grid()
        self.bttn_home = Button(self, text = "Home Team Scores!", command = self.home_button)
        self.bttn_home.grid()
        self.bttn_visitor = Button(self, text = "Visiting Team Scores!", command = self.visitor_button)
        self.bttn_visitor.grid()

    def home_button(self):
        self.bttn_clicks += 1
        self.lbl_home["text"] = "Home Team: " + str(self.bttn_clicks)
        self.winning_label()

    def visitor_button(self):
        self.bttn_clicks_visitor += 1
        self.lbl_visitor["text"] = "Visitors: " + str(self.bttn_clicks_visitor)
        self.winning_label()

    def winning_label(self):
        if self.bttn_clicks > self.bttn_clicks_visitor:
            self.lbl_winning["text"] = "Winning: Home Team"
        elif self.bttn_clicks < self.bttn_clicks_visitor:
            self.lbl_winning["text"] = "Winning: Visitors"
        else:
            self.lbl_winning["text"] = "Tie!"
    
            
            

    

    
                           


# main
root = Tk()
root.title("Game Tracker")
root.geometry("200x200")
root.resizable(width = TRUE, height = TRUE)

app = Application(root)
root.mainloop()

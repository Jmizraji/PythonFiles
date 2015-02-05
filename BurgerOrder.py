from Tkinter import *

class Application(Frame):
    """ GUI application which can reveal the secret of longevity. """
    def __init__(self, master):
        """ Initialize the frame. """
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry widgets. """
        Label(self, text="Name:").grid(row = 1, column = 0, sticky = W)
        
        self.name = Entry(self)
        self.name.grid(row = 1, column = 0, columnspan = 1)

        Label(self, text="Please select what you would like on your burger.").grid(row = 2, \
                                                                                   column = 0, \
                                                                                   sticky = W)                                                                             

        # Cheese Button
        self.cheese = BooleanVar()
        Checkbutton(self, text = "Cheese", variable = self.cheese).grid(row = 3, column = 0, sticky = W)

        # Lettuce Button
        self.lettuce = BooleanVar()
        Checkbutton(self, text = "Lettuce", variable = self.lettuce).grid(row = 4, column = 0, sticky = W)
                    

        # Onion Button
        self.onion = BooleanVar()
        Checkbutton(self, text = "Onion", variable = self.onion).grid(row = 5, column = 0, sticky = W)

        # Tomato Button
        self.tomato = BooleanVar()
        Checkbutton(self, text = "Tomato", variable = self.tomato).grid(row = 6, column = 0, sticky = W)

        # Pickles Button
        self.pickles = BooleanVar()
        Checkbutton(self, text = "Pickles", variable = self.pickles).grid(row = 7, column = 0, sticky = W)

        # Mustard Button
        self.mustard = BooleanVar()
        Checkbutton(self, text = "Mustard", variable = self.mustard).grid(row = 8, column = 0, sticky = W)

        # Mayo Button
        self.mayo = BooleanVar()
        Checkbutton(self, text = "Mayo", variable = self.mayo).grid(row = 9, column = 0, sticky = W)

        # Ketchup Button
        self.ketchup = BooleanVar()
        Checkbutton(self, text = "Ketchup", variable = self.ketchup).grid(row = 10, column = 0, sticky = W)

        # White or Wheat Button
        self.white = BooleanVar()
        self.wheat = BooleanVar()
    
        
        Checkbutton(self, text = "White Bun", variable = self.white).grid(row = 11, column = 0, sticky = W)
        Checkbutton(self, text = "Wheat Bun", variable = self.wheat).grid(row = 11, column = 0, columnspan = 1)

        #Order Button
        self.order_button = Button(self, text="Order Up!", command = self.update_text)
        self.order_button.grid(row = 13, column = 0, sticky = W)

        # Order Text Box
        self.order_box = Text(self, width = 35, height = 10, wrap = WORD)
        self.order_box.grid(row = 14, column = 0, columnspan = 2, sticky = W)
        
        


    def update_text(self):
        final_order = self.name.get() + " ordered a burger with "
        if self.cheese.get():
            final_order += "cheese, "

        if self.lettuce.get():
            final_order += "lettuce, "

        if self.onion.get():
            final_order += "onion, "

        if self.tomato.get():
            final_order += "tomato, "

        if self.pickles.get():
            final_order += "pickles, "

        if self.mustard.get():
            final_order += "mustard, "

        if self.mayo.get():
            final_order += "mayo, "

        if self.ketchup.get():
            final_order += "ketchup, "

        
        if self.white.get():
            final_order += "and a white bun."
    
        if self.wheat.get():
            final_order += "and a wheat bun."
        if self.wheat.get() == self.white.get():
            Label(self, text="Please select EITHER a White or Wheat Bun", bg = "red").grid(row = 12, column = 0, sticky = W)
            error_text = "ORDER ERROR!"
            self.order_box.delete(0.0,END)
            self.order_box.insert(0.0, error_text)
        else:
            self.order_box.delete(0.0,END)
            self.order_box.insert(0.0, final_order)

     




root = Tk()
root.title("Order A Burger")
root.geometry("410x480")
root.resizable(width = TRUE, height = TRUE)

app = Application(root)
root.mainloop()

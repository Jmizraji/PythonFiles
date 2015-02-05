
import random 
from Tkinter import *

class Application(Frame):

    def __init__(self, master):   
        Frame.__init__(self, master)
        self.grid() 
        self.create_widgets()

        
    def create_widgets(self):
        Label(self, text = "Welcome: Please select your racecar options").grid(row = 0,column = 4, columnspan = 4)
        Label(self, text = "Driver:").grid(row = 1, column = 0)

        #Driver Entry
        self.driver_entry = Entry(self, width = 50)
        self.driver_entry.grid(row = 1, column = 4, columnspan = 3, sticky = W)

        #Race Conditions
        Label(self, text = "Race Conditions:").grid(row = 2, column = 3,sticky = W)
        
        self.rainy = BooleanVar()
        Checkbutton(self, text = "Rainy", variable = self.rainy).\
                          grid(row = 3, column = 3,sticky = W)

        self.windy = BooleanVar()
        Checkbutton(self, text = "Windy", variable = self.windy).\
                          grid(row = 4, column = 3,sticky = W)

        #Engine
        Label(self, text = "Engine:").grid(row = 2, column = 4,sticky = W)

        self.favorite = StringVar()
        self.favorite.set(500)
        Radiobutton(self, text = "Gas ($500)", variable = self.favorite, value = 500, command = self.update_spent).\
                          grid(row = 3, column = 4,sticky = W)
        
        Radiobutton(self, text = "Diesel ($1000)", variable = self.favorite, value = 1000,command = self.update_spent).\
                          grid(row = 4, column = 4,sticky = W)

        Radiobutton(self, text = "Electric ($2000)", variable = self.favorite, value = 2000,command = self.update_spent).\
                          grid(row = 5, column = 4,sticky = W)

        #Car
        Label(self, text = "Car:").grid(row = 2, column = 5,sticky = W)

        self.favorite2 = StringVar()
        self.favorite2.set(1500)
        Radiobutton(self, text = "Lotus ($1500)", variable = self.favorite2, value = 1500,command = self.update_spent).\
                          grid(row = 3, column = 5,sticky = W)
        
        Radiobutton(self, text = "Mercedes ($2500)", variable = self.favorite2, value = 2500,command = self.update_spent).\
                          grid(row = 4, column = 5,sticky = W)

        Radiobutton(self, text = "McLaren ($3500)", variable = self.favorite2, value = 3500,command = self.update_spent).\
                          grid(row = 5, column = 5,sticky = W)
        

        #Total Spent
        Label(self, text = "Total Spent: $ 2000").grid(row = 6, column = 2 ,columnspan = 2, sticky = W)

        #Budget
        self.budget = Label(self, text = "You are under your budget of $4000")
        self.budget.grid(row = 6, column = 5 ,columnspan = 3, sticky = W)
        self.update_spent()

        #Run Race Button
        self.race_button = Button(self, text = "Run Race", command = self.update_text)
        self.race_button.grid(row = 7, column = 4)

        #text Box
        self.text_box = Text(self, width = 85, height = 5, wrap = WORD)
        self.text_box.grid(row = 8, column = 0, columnspan = 8, sticky = W)
        
    def update_spent(self):
        total_spent = 0

        if self.favorite.get():
            total_spent += int(self.favorite.get())

        if self.favorite2.get():
            total_spent += int(self.favorite2.get())

        Label(self, text = "Total Spent: $" + str(total_spent)).grid(row = 6, column = 2 ,columnspan = 2, sticky = W)

        if total_spent <= 4000:
            self.budget["text"] = "You are under your budget of $4000"
        else:
            self.budget["text"] = "Warning! You are over your budget of $4000"

    def update_text(self):
        race_results = ""

        if self.favorite2.get() == "3500":
            random_number = random.randrange(11)
            if random_number != 1:
                race_results += "Congradulations "
                if self.driver_entry.get():
                    race_results += self.driver_entry.get() + ", you won the race while driving a McClaren with a "
                if self.favorite.get() == "500":
                    race_results += "gas engine in"
                if self.favorite.get() == "1000":
                    race_results += "diesel engine in"
                if self.favorite.get() == "2000":
                    race_results += "electric engine in"
                if self.rainy.get():
                    race_results += " rainy"
                if self.windy.get():
                    race_results += " windy"
                if self.windy.get() == False and self.rainy.get() == False:
                    race_results += " nice"
                race_results += " conditions."
            else:
                race_results += "Sorry "
                if self.driver_entry.get():
                    race_results += self.driver_entry.get() + ", you lost the race while driving a McClaren with a "
                if self.favorite.get() == "500":
                    race_results += "gas engine in"
                if self.favorite.get() == "1000":
                    race_results += "diesel engine in"
                if self.favorite.get() == "2000":
                    race_results += "electric engine in"
                if self.rainy.get():
                    race_results += " rainy"
                if self.windy.get():
                    race_results += " windy"
                if self.windy.get() == False and self.rainy.get() == False:
                    race_results += " nice"
                race_results += " conditions."

        if self.favorite2.get() == "2500":
            random_number = random.randrange(2)
            if random_number != 1:
                race_results += "Congradulations "
                if self.driver_entry.get():
                    race_results += self.driver_entry.get() + ", you won the race while driving a Mercedes with a "
                if self.favorite.get() == "500":
                    race_results += "gas engine in"
                if self.favorite.get() == "1000":
                    race_results += "diesel engine in"
                if self.favorite.get() == "2000":
                    race_results += "electric engine in"
                if self.rainy.get():
                    race_results += "rainy"
                if self.windy.get():
                    race_results += " windy"
                if self.windy.get() == False and self.rainy.get() == False:
                    race_results += " nice"
                race_results += " conditions."
            else:
                race_results += "Sorry "
                if self.driver_entry.get():
                    race_results += self.driver_entry.get() + ", you lost the race while driving a Mercedes with a "
                if self.favorite.get() == "500":
                    race_results += "gas engine in"
                if self.favorite.get() == "1000":
                    race_results += "diesel engine in"
                if self.favorite.get() == "2000":
                    race_results += "electric engine in"
                if self.rainy.get():
                    race_results += " rainy"
                if self.windy.get():
                    race_results += " windy"
                if self.windy.get() == False and self.rainy.get() == False:
                    race_results += " nice"
                race_results += " conditions."

        if self.favorite2.get() == "1500":
            random_number = random.randrange(2)
            if random_number != 1:
                race_results += "Congradulations "
                if self.driver_entry.get():
                    race_results += self.driver_entry.get() + ", you won the race while driving a Lotus with a "
                if self.favorite.get() == "500":
                    race_results += "gas engine in"
                if self.favorite.get() == "1000":
                    race_results += "diesel engine in"
                if self.favorite.get() == "2000":
                    race_results += "electric engine in"
                if self.rainy.get():
                    race_results += " rainy"
                if self.windy.get():
                    race_results += " windy"
                if self.windy.get() == False and self.rainy.get() == False:
                    race_results += " nice"
                race_results += " conditions."
            else:
                race_results += "Sorry "
                if self.driver_entry.get():
                    race_results += self.driver_entry.get() + ", you lost the race while driving a Lotus with a "
                if self.favorite.get() == "500":
                    race_results += "gas engine in"
                if self.favorite.get() == "1000":
                    race_results += "diesel engine in"
                if self.favorite.get() == "2000":
                    race_results += "electric engine in"
                if self.rainy.get():
                    race_results += " rainy"
                if self.windy.get():
                    race_results += " windy"
                if self.windy.get() == False and self.rainy.get() == False:
                    race_results += " nice"
                race_results += " conditions."
            
                    
            

            
                
            
            


        
            
        self.text_box.delete(0.0,END)
        self.text_box.insert(0.0, race_results)           

    
            
        

        

        
        



# main
root = Tk()   
root.title("Racing Sim")
root.geometry("700x300")  
app = Application(root) 
root.mainloop()  

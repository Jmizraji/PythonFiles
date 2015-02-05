#This program simulates a tv

class Television(object):


    def __init__(self, channel):
        self.__channel = channel
        self.volume = 5
        self.is_on = False
        

    def toggle_power(self):
        if self.is_on == True:
            self.is_on = False
        else:
            self.is_on = True

    def get_channel(self):
        self.current_channel = self.__channel
        return self.current_channel

    def set_channel(self):
        self.new_channel = int(raw_input("Please pick a number between 0-499 to change the channel to: "))
        if self.is_on == True:
            if self.new_channel >= 0 and self.new_channel <= 499:
                self.__channel = self.new_channel
            else:
                print "I'm sorry, that is not a valid channel"
        else:
            print "Please turn the TV to change the channel"

    def raise_volume(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print "The volume is already at the maximum level 10!"
    
    def lower_volume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print "The volume is already at the lowest level 0!"

    def __str__(self):
        if self.is_on == True:
            reply = "The Television is On \n"
            reply += "Current Channel: " + str(self.__channel)+"\n"
            reply += "Current Volume: " + str(self.volume)+"\n"
            return reply
        else:
            reply = "The Television is Off\n"
            return reply



def main():
    choice = None
    while choice != "0":
        print\
        """
        This is your Virtual TV!

        0 - Exit
        1 - Toggle Power
        2 - Change Channel
        3 - Raise Volume
        4 - Lower Volume
        """

        choice = raw_input("Choice: ")
        print

        #exit
        if choice == "0":
            print "Menu Exited"

        # Toggle Power
        elif choice == "1":
            tv.toggle_power()
            print tv
            
            

        # Change Channel
        elif choice == "2":
            tv.set_channel()
            tv.get_channel()
            print tv
            
            

        # Raise Volume
        elif choice == "3":
            tv.raise_volume()
            print tv
 
        # Lower Volume
        elif choice == "4":
            tv.lower_volume()
            print tv
            

        elif choice == "":
            break
        # some unknown choice
        else:
            print "\nSorry, but", choice, "isnt't a valid choice."




#test code
tv = Television(2)


main()

("\n\nPress the enter key to exit.")


        

    

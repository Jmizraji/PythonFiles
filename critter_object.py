#Critter Caretaker
#A virtual pet to care for

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __get_mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            mood = "happy"
        elif 5 <= unhappiness <= 10:
            mood = "okay"
        elif 11 <= unhappiness <+ 15:
            mood = "frustrated"
        else:
            mood = "mad"
        return mood

    mood = property(__get_mood)

    def talk(self):
        print "I'm", self.name, "and I feel", self.mood, "now.\n"
        self.__pass_time()

    def eat(self, food):
        print "Brruppp. Thank you."
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):
        print "Wheee!"
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self):
        reply = "Critter name: " + self.name
        reply += "\nHunger: " + str(self.hunger)
        reply += "\nBoredom: " + str(self.boredom)
        return reply
    


def main():
    crit_name = raw_input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print\
        """
        Critter Caretaker

        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """

        choice = raw_input("Choice: ")
        print

        #exit
        if choice == "0":
            print "Good-bye."

        # listen to your critter
        elif choice == "1":
            crit.talk()

        # feed your critter
        elif choice == "2":
            food = int(raw_input("How much food would you like to feed " + crit_name + "? "))
            print
            while food < 1:
                print "Sorry, but", food, "isn't a valid choice. Please enter a number greater than 0."
                food = int(raw_input("How much food would you like to feed " + crit_name + "? "))
                print
                
            crit.eat(food)

        # play with your critter
        elif choice == "3":
            fun = int(raw_input("How much fun would you like to have with " + crit_name + "? "))
            print
            while fun < 1:
                print "Sorry, but", fun, "isn't a valid choice. Please enter a number greater than 0."
                fun = int(raw_input("How much fun would you like to have with " + crit_name + "? "))
                print

            crit.play(fun)

        # unlisted choice. displays exact values of your critter's attributes
        elif choice == "-1":
            print crit
            
        # some unknown choice
        else:
            print "\nSorry, but", choice, "isn't a valid choice."


main ()
("\n\nPress the enter key to exit.")

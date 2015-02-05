import random

class Animal(object):

    def __init__(self, species, name):
        self.species = species
        self.name = name
        self.hunger = 0
        self.visible = True

    def __str__(self):
        reply = self.species + "Name:"+ self.name + "\n"
        if self.hunger >= 5:
            reply += "Status: HUNGRY" + "\n"
        elif self.hunger >= 3 and self.hunger <= 4:
            reply += "Status: Somewhat Hungry" + "\n"
        elif self.hunger < 3:
            reply += "Status: Fine" + "\n"
        return reply

    def pace(self):
        if self.visible:
            self.hunger += 1
            if self.hunger >= 5:
                self.visible = False
                print "EXHIBIT CLOSED: " + self.name + "!\n"
        else:
            print "EXHIBIT CLOSED: " + self.name + "!\n"
            
class Zoo(object):

    def __init__(self,name):
        self.animals = []
        self.keeper_name = name
        self.opens = []
        self.closed = []
        

    def open_exhibits(self):
        self.opens = []
        reply = "OPEN Exhibits:\n"
        for creature in self.animals:
            if creature.visible:
                self.opens.append(creature)
        if self.opens:
            for creature in self.opens:
                reply += str(creature) + "\n"
        else:
            reply += "None"                   
        return reply
    
    def closed_exhibits(self):
        self.closed = []
        reply = "ClOSED Exhibits:\n"
        for creature in self.animals:
            if creature.visible == False:
                reply += str(creature) + "\n"
        if self.closed:
            for creature in self.closed:
                reply += str(creature) + "\n"
        else:
            reply += "None"       
        return reply

    def work(self):
            random_animal = (random.choice(self.animals))
            if random_animal.visible == True:
                random_animal.hunger = 0
                print self.keeper_name + " puts food out for " + random_animal.name
                for creatures in self.animals:
                    if creatures != random_animal:
                        creatures.pace()                   
                print "All of the other animals pace in their enclosure"
                print "-" * 25
            

    def run(self):
        self.day = 1
        self.closed_exhibit = 0
        print self.keeper_name + " begins work!"
        print
        while self.closed_exhibit < 2:           
                print "It's day " + str(self.day)
                print
                self.day += 1
                self.work()
                for creature in self.animals:
                    if creature.visible != True:
                        self.closed_exhibit += 1
        print "*" * 25
        print "The zoo closed on day " + str(self.day)
        print
        print self.open_exhibits()
        print self.closed_exhibits()
        
    
       
# TEST CODE
barnum = Zoo("Fred")
barnum.animals.append(Animal("Tiger","Stripes")) 
barnum.animals.append(Animal("Monkey","Aldo"))
barnum.animals.append(Animal("Monkey","Mandemus"))
barnum.animals.append(Animal("Monkey","Dr. Milo"))
barnum.animals.append(Animal("Seal","Hoover"))
barnum.animals.append(Animal("Penguin","Salty"))

barnum.run()




                      

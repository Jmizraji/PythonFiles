class Fish(object):
    school = []
    
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.caught = False
        Fish.school.append(self)
        print "Fish put in pond:",self.name

    def __str__(self):
        reply = "Name: " + self.name + "\n"
        reply += "Length: " + str(self.length) + "\"" + "\n"
        if self.caught == False:           
            reply += "Status: FREE\n"
        else:
            reply += "Status: CAUGHT"
        return reply

    def __cmp__(self, other):
        if self.length > other.length:
            return 1
        elif self.length == other.length:
            return 0
        else:
            return -1
        
    @staticmethod
    def remaining():
        print "Number of fish in the pond:",len(Fish.school)
        for fish in Fish.school:
            print fish

    @staticmethod
    def largest():
        print "The largest fish is: ",max(Fish.school).name
            

    def catch(self):
        print "You attempt to catch",self.name +".",
        if self.caught == False:
            self.caught = True
            print "Success!"
            print self
        else:
            print self.name, "was already caught!"
            

#test code
fish1 = Fish("Bass", 10)
fish2 = Fish("Goldfish", 2)
fish3 = Fish("Shark", 50)
Fish.remaining()
Fish.largest()
fish1.catch()
Fish.remaining()


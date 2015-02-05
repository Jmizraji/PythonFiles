class Fish(object):
    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.caught = False
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
print fish3
print fish1.name, "is longer than", fish2.name, ":", fish1 > fish2
print fish1.name, "is longer than", fish3.name, ":", fish1 > fish3
fish1.catch()
fish1.catch()

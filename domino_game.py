class Domino(object):

    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def __str__(self):
        #you don't need to modify this!
        return "|" + str(self.head) + ":" + str(self.tail) + "|"

    def flip(self):
        self.head,self.tail = self.tail,self.head

    def fits(self, other):
        if (self.head or self.tail == other.head) or (self.tail or self.head == other.tail):
            return True
        else:
            return False

class Chain(object):

    def __init__(self):
        self.dominoes = []
        self.chain = []

    def __str__(self):                 
        reply = "Current chain: "
        for element in self.chain:
            reply += str(self.chain.index(element)) + " - " + str(element)+ "\t"
        reply += "\nAvailable dominoes: "
        for element in self.dominoes:
            reply += str(self.dominoes.index(element)) + " - " + str(element)+ "\t"
        return reply

    def add(self, domino):
        #you don't need to modify this!
        self.dominoes.append(domino)

    def play(self, num):
        print self
        reply = "Attempting to add domino " + str(self.dominoes[num]) + " to the chain."                 
        if not self.chain :
            self.chain.append(self.dominoes[num])
            self.dominoes.remove(self.dominoes[num])
            reply += "\n" + str(self.dominoes[num]) + " added to the current chain"
        elif self.dominoes[num].fits(self.chain[-1]):
            self.chain.append(self.dominoes[num])
            self.dominoes.remove(self.dominoes[num])
            reply +=  str(self.dominoes[num]) + " added to the current chain"
        else:
            reply +=  str(self.dominoes[num]) + " doesn't fit in the current chain!"
        print reply
        
            
        #here we should attempt to add a domino to the chain
        #and print out success or failure
        #num will determine where the domino is in the list
        

    def moves(self, num_list): 
        #given a list of index numbers, we try to make those plays in that order
        for element in num_list:
            self.play(element) 
            

#main - test code
my_chain = Chain()
my_chain.add(Domino(2,3))
my_chain.add(Domino(6,4))
my_chain.add(Domino(1,3))
my_chain.add(Domino(4,1))

#when a domino is played, it's removed from the list, so
#this next line is not just playing the same two dominoes
my_chain.moves([0,1,0,1,0])
print my_chain

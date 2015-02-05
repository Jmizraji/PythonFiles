

import random
#############
class Investment(object):

    investment_list = []
    
    def __init__(self, name, initial_balance):
        self.name = name
        self.initial_balance = float(initial_balance)
        self.current_balance = float(initial_balance)
        Investment.investment_list.append(self) 

    def __str__(self):
        reply = "Investment: " + self.name + "\n"
        reply += "\tInitial balance: $" + str(self.initial_balance) + "\n"
        reply += "\tCurrent balance: $" + str(self.current_balance) + "\n"
        return reply

    def __cmp__(self, other):        
        if self.current_balance > other.current_balance:
            return 1
        elif self.current_balance < other.current_balance:
            return -1
        else:
            return 0

    @staticmethod
    def losers():
        for investments in Investment.investment_list:
            if investments.current_balance < investments.initial_balance:
                print investments
            else:
                print

    def swap(self, other):
        #This should move the current_balance of 1 investment to the other, leaving the initial_balance
        #and names the same
        self.current_balance,other.current_balance = other.current_balance,self.current_balance


class SavingsAccount(Investment):

    def __init__(self, name, initial_balance,interest_rate):
        super(SavingsAccount,self).__init__(name, initial_balance)
        self.interest_rate = interest_rate

    def __str__(self):
        reply = "SavingsAccount Investment: " + self.name + "\n"
        reply += "\tInitial balance: $" + str(self.initial_balance) + "\n"
        reply += "\tCurrent balance: $" + str(self.current_balance) + "\n"
        reply += "\tInterest rate: " + str(self.interest_rate) + "%\n"
        return reply

    def annual_update(self):
        if self.current_balance >= 1000:
            self.current_balance += round(self.current_balance * (self.interest_rate * .01),2)
        else:
            self.current_balance -= 10

class PreciousMetal(Investment):

    def __init__(self, name, initial_balance):
        super(PreciousMetal,self).__init__(name, initial_balance)
        

    def __str__(self):
        reply = "PreciousMetal Investment: " + self.name + "\n"
        reply += "\tInitial balance: $" + str(self.initial_balance) + "\n"
        reply += "\tCurrent balance: $" + str(self.current_balance) + "\n"
        return reply

    def annual_update(self):
        random_number =  random.randrange(1,11,1)
        if random_number == 2:
            self.current_balance = 0
        else:
            random_percentage = random.randrange(-5,10,1)
            self.current_balance += round(self.current_balance * (random_percentage * .01),2) 


#############



def print_investments(investments):
    print "Current investments are:"    
    for i in investments: 
        print i


#### Main body
#

# Welcome message. 
print "Welcome to the I210 investment tracking system!"  
print "(This version is by " + "Joshua Mizraji, id=jomizraj)"   
print ""

current_step = int(raw_input("Which Step would you like to test? (Enter 2,3,or 4): "))

if current_step == 2:
    investments = [Investment("Gold", 500.37), Investment("Pork bellies", 125.69), Investment("Apple stock", 1035.34)]

    # modify each account by a random amount
    for i in investments:
        i.current_balance += random.randrange(-100, 100)

    print_investments(investments)

    print "The smallest investment is:"
    print sorted(investments)[0]

    print "Swapping", investments[0].name, "and", investments[1].name, "..."
    investments[0].swap(investments[1])

    print "The losing investments are:"
    Investment.losers()

elif current_step == 3:
    investments = [ PreciousMetal("Gold", 3000.00), \
                        SavingsAccount("HSBC", 5432.00, 2), \
                        SavingsAccount("Cherry Bank", 999.0, 5)]  # this means initial balance $999, 5% interest

    print_investments(investments)

    # let the investments grow for 5 years!
    print "Investing for 5 years...\n\n"
    for year in range(2004,2009):
        for i in investments:
            i.annual_update()

    print_investments(investments)

elif current_step == 4:
    own_investments = []
    print "Let's add our own accounts!"
    investment_type = raw_input("What type of investment are you making? ")
    init_balance = raw_input("What is the initial balance of the investment? ")
    years = raw_input("Enter the number of years on investment: ") 
    own_investments.append(PreciousMetal(investment_type,float(init_balance)))
    for year in range(int(years)):
        for i in own_investments:
            i.annual_update()
    print_investments(own_investments)
                          

else:
    print "Enter 2 or 3!"

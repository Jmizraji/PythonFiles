#This is a car racing game
import random 
class Car(object):
    """A virtual race car"""

    def __init__(self, make,driver):
        #constructor
        self.miles = 0
        self.make = make
        self.driver = driver
    
    def drive(self):
        lap_number = 0
        while self.miles < 500:
            lap_number += 1
            print "Lap:" + str(lap_number)
            if self.driver == "Tony Stewart":
                if self.make == "Ferrari":
                    self.miles += random.randrange(10,91,1) + 10                               
                elif self.make == "Porsche":
                    self.miles += random.randrange(30,70,1) + 10
                else:
                    self.miles += 50 + 10
            else:
                if self.make == "Ferrari":
                    score1 = random.randrange(10,91,1)
                    score2 = random.randrange(10,91,1)
                    if score1 > score2:
                        self.miles += score1
                    else:
                        self.miles += score2
                elif self.make == "Porsche":
                    score1 = random.randrange(30,70,1)
                    score2 = random.randrange(30,70,1)
                    if score1 > score2:
                        self.miles += score1
                    else:
                        self.miles += score2 
                else:
                    self.miles += 50
            print self.driver + " drove " + str(self.miles) + " miles."
           

        
             

    def __str__(self):
  
        reply = ""
        return reply



# main
print """
Welcome to the race!
----------------------------------------------
Each Player, please select your car and driver.
Cars are BMW,Porsche, and Ferrari
Drivers are Mario Andretti and Tony Stewart"""
print

player1_make = raw_input("Player 1, please enter your car: ")
player1_driver = raw_input("Player 1, please enter your driver: ")
player2_make = raw_input("Player 2, please enter your car: ")
player2_driver = raw_input("Player 2, please enter your driver: ")


player1 = Car(player1_make,player1_driver)
player2 = Car(player2_make, player2_driver)
player1.drive()
player2.drive()
print

if player1.miles > player2.miles:
    print "Congradulations! Player 1 with",player1.driver,"driving a" \
          ,player1.make,",you are the winner!"
elif player1.miles < player2.miles:
    print "Congradulations! Player 2 with",player2.driver,"driving a" \
          ,player2.make,",you are the winner!"
else:
    print "It's a tie!" 





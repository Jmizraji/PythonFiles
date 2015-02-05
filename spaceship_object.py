class Ship(object):
    def __init__(self, name = "Enterprise", fuel = 0):
        self.name = name
        if fuel < 0:
            self.fuel = 0
        else:
            self.fuel = fuel

    def status(self):
        print "Name:", self.name
        print "Fuel Level:", self.fuel

    def move(self, distance):
        self.distance = distance
        if self.distance <= 1:
            print "\nThe ship can't move a distance less than 1"
            self.status()
        else:
            if self.distance <= self.fuel:
                self.fuel -= self.distance
                print "\nThe ship has moved " + str(self.distance) + " space measurements and the fuel level" \
                      + " is at " + str(self.fuel) 
                self.status()
            elif self.distance >= self.fuel:
                print "\nThe ship doesn't have enough fuel to move"
                self.status()

    def refuel(self, fuel_amount):
        self.fuel_amount = fuel_amount
        if self.fuel_amount >= 1:
            self.fuel += self.fuel_amount
            print "\nFuel has been added!"
            self.status()
        else:
            print "\nThe ship can't be refueled with an amount less than 1"
            self.status()
        

#tests
#default ship
ship1 = Ship()

#different name, default fuel
ship2 = Ship("Ship Name")

#default name, different fuel
ship3 = Ship(fuel = 700)

#different name and fuel
ship4 = Ship("Other Name", 500)

ship1.status()
print
ship2.status()
print
ship3.status()
print
ship4.status()

ship1.move(234)
ship1.move(1)
ship1.refuel(0)
ship1.refuel(231)

ship4.move(234)
ship4.move(1)
ship4.refuel(0)
ship4.refuel(231)




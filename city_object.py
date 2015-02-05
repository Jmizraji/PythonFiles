import random

class City(object):

    city_list = []

    def __init__(self, name,population,location):
        self.__name = name
        self.population = int(population)
        self.__location = location
        print "New City: " + self.__name 
        City.city_list.append(self) 
    
    def __str__(self):
        reply = "\nCity: " + self.__name + "\n"
        reply += "Population: " + str(self.population) + "\n"
        reply += "Location: " + self.__location + "\n"
        return reply
        
    def migrate(self, other):
        random_number = random.randrange(20001)
        self.population = self.population - random_number
        other.population = other.population + random_number
        return "\nPopulation of " + self.__name + "\nhas decreased by " + str(random_number) \
              + " and" + "\nthe population of " + other.__name + "\n" \
              + "has increased by " + str(random_number)

    def __cmp__(self, other):        
        if self.population > other.population:
            return 1
        elif self.population < other.population:
            return -1
        else:
            return 0

    @staticmethod
    def cities_in(city_we_are_looking_for):
        print "\nCities in " + city_we_are_looking_for
        for c in City.city_list:
            if c.__location == city_we_are_looking_for:
                print c.__name

    @staticmethod
    def save_file(filename):
        file = open(filename, "w")
        for c in City.city_list:
            file.write(str(c))
        file.close()
            
            
         

def main():
    #create cities
    nyc = City("New York City", "8400000", "NY")
    chicago = City("Chicago", "2700000", "IL")
    bloomington = City("Bloomington", "82000", "IN")
    indianapolis = City("Indianapolis", "852000", "IN")
    sanfran = City("San Francisco", "2700000", "CA")


    
    #change city pop
    print nyc.migrate (chicago)

    #print city information
    print chicago
    print nyc 
    
    #compare cities
    print "Chicago is larger than NYC:", chicago > nyc
    print "Bloomington is the same size as Indianapolis:", bloomington == indianapolis
    print "San Francisco is the same size as Chicago:", sanfran == chicago
    
    #print all cities in IN
    City.cities_in("IN")
   
    #save data
    print City.save_file("Cities.txt")
    
main()

#Class and Functions

class Player(object):
    items_list=[]
    
    def __init__(self,name):
        self.name=name
        self.max_items=5
        print "The player is " + self.name +"."

    def inventory(self):
        if self.items_list:
            print self.items_list
        else:
            print self.name + " has no items!"

    
    def take(self,item):
        if len(self.items_list) < self.max_items:
            self.items_list.append(item)
            print item, " has been added to the list."
            print self.items_list
        else:
            print self.name + " cannot take more items!"

    def drop(self,item):
        if item in self.items_list:
            self.items_list.remove(item)
            print item, " has been removed from the list."
            print self.items_list
        else:
            print self.name +" does not carry that item!"

#main
#create the player
player = Player("Jose")

#create the list of items
player.items_list=["Mitt","Glove","Bat","Ball","Computer"]
player.inventory()

#Take more items than he can hold
player.take("Sand")

#Drop an item
player.drop("Mitt")

#Take an item that was previously not in list
player.take("Fork")

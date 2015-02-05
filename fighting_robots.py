import random

class Robot(object):
    """Virtual Fighting Robots"""

    robot_list = []

    @staticmethod
    def contenders():
        print "There are",len(Robot.robot_list),"robots."
        print "Here is a list of them:"
        for item in Robot.robot_list:
            print item

    def fight(self,challenger):
        print self.name,"challenges",challenger.name
        print "Close match!!!"
        if self.online == challenger.online:
            if self.strength > challenger.strength:
                print self.name,"wins, using its",self.weapon
                challenger.online = False
            elif self.strength < challenger.strength:
                print challenger.name,"wins, using its", challenger.weapon
                self.online = False
            else:
                win = random.randrange(0,2)
                if win:
                    print self.name,"wins, using its",self.weapon
                    challenger.online = False
                else:
                    print challenger.name,"wins, using its", challenger.weapon
                    self.online = False
            print self
            print challenger
        else:
            if self.online:
                print challenger.name, "cannot fight - it is offline"
            else:
                print self.name, "cannot fight - it is offline"
        
                
                
        

    def __init__(self,name,weapon,strength):
        print "Robot created!",name,"\n"
        self.name = name
        self.weapon = weapon
        self.strength = strength
        self.online = True
        if name not in Robot.robot_list:
            Robot.robot_list.append(self) 
        
             
            

    def __str__(self):
        reply = "-"*20+"\n"
        reply += "Fighting Robot \n"
        reply += "Name:" + self.name +"\n"
        reply += "Weapon:"+ self.weapon +"\n"
        reply += "Strength:" + str(self.strength) + "\n"
        if self.online == True:
            reply += "Status: Online \n"
        else:
            reply += "Status: Offline \n"
        reply += "-"*20+"\n"
        return reply
         
        
   

#main section of the code

r2d2 = Robot("R2D2","Beeps",2)
c3po = Robot("C3PO","Conversation",2)

r2d2.fight(c3po)
r2d2.fight(c3po)



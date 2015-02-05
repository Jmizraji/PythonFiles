# This program tells tells the story of a brave band of explorers

print """Welcome to the Lost Fortune!

Please enter your personalized adventure: """

number_of_explorers = int(raw_input("Enter the number of explorers: "))
number_of_explorers_lost = int(raw_input("Enter the number of explorers lost in battle: "))
quest_leader = str(raw_input("Enter the name of the quest leader: ")) 

print "The brave",quest_leader,"led",number_of_explorers,"adventureres on a quest for gold."
print "The group fought a band of ogres and lost",number_of_explorers_lost,"members."

number_of_explorers_survived = number_of_explorers - number_of_explorers_lost

print "Only",number_of_explorers_survived,"survived."

extra_pieces = 750 % number_of_explorers_survived 

print """The party was about to give up when they stumbled upon the buried fortune
of 750 gold pieces. They split the loot and""",quest_leader,"kept the extra",extra_pieces,"pieces."




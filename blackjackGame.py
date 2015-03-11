import random as r


#initialize all suits
suits = ['Sp','Cl','He','Di']
#initialize all values
numb= ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

#set values for cards in a dictionary(solves the j,q,k,a value issue)
value_dic= {'2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','1':'10','J':'10','Q':'10','K':'10','A':'11'}
#note Ace  is set to default of 11, whereas in Blackjack it could be 11 or 1.......
#also note the key in the dictionary for '10' is actially 1, as there is no '1' in a deck of cards


#generate a list of all cards in the deck (no joker)
deck =[numb[i]+suits[j] for i in range(len(numb)) for j in range(len(suits))]
print "check my deck: ",deck,"\n"
print "-"*20

#printing the value of each card in the deck
values =[int(value_dic.get(deck[i][0],'That\'s not a real card...')) for i in range(len(deck))]
print "here is how each card in the deck is currently valued",values
print "-"*20,"\n"


#shuffle the deck
r.shuffle(deck)
print "the deck shuffled:",deck,"\n"
print "-"*20



#Deal Hands of black jack..use randomly 2-5 cards
#continue dealing random hands until you get a total of 21
hand_value= 0
while hand_value!= 21:
    #create the hand
    hand= [r.choice(deck) for i in range(r.randrange(2,6)) ]
    print 'your hand is:',hand
    
    #creating an integer from a list!?
    #Woah!>Note: all list comprehensions can do is create lists...must use sum() to return an int
    hand_value= sum([int(value_dic.get(hand[i][0],'That\'s not a real card...')) for i in range(len(hand))])
    print "your hand is valued at: ",hand_value,"\n\n"

#Congrats you generated a blackjack
print 'blackjack!\n\n\n'


print "-"*20
print "PART 2!"
print "-"*20

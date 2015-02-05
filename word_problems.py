# This program solves some word problems

friends = int(raw_input("How many friends are you buying cookies for? "))

"""You buy x friends 2 cookies each. You also buy 1 for your professor. How many
do you buy"""

cookie_amount = (friends * 2) + 1

print "You bought",cookie_amount,"cookies"

""" You split y pieces of pizza among 5 people. How many are left over if
you all get an equal share?"""

pieces = int(raw_input("How many pieces of pizza are there? "))

left_over = pieces % 5

print "You have",left_over, "pieces left"

"""The bill for the food was z dollars. If there are 5 people, how much does
each person pay?"""

bill = float(raw_input("How much was the bill? "))

person_paid = bill / 5
person_paid_rounded = round(person_paid, 2)

print "Each person pays $" + str(person_paid_rounded) 

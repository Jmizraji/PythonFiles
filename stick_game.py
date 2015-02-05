#The game asks each player how many sticks they want to take (1-4) from the
#pile, and continues until the pile reaches 0. The last person to take a stick
#is the winner.


#variables
pile = 13
maximum = 4
minimum = 1
player = 1
sticks_taken = int(raw_input("How many sticks do you want to take, Player 1 (between 1 & 4)? "))

#loop
while pile:
    if player == 1:
        if (sticks_taken > pile) or (sticks_taken > 4) or (sticks_taken < 1):
            sticks_taken = int(raw_input("Please enter a legal value (1-4): "))
        else:
            pile -= sticks_taken
            print "There are", pile, "sticks left."
            if pile == 0:
                break
            sticks_taken = int(raw_input("How many sticks do you want to take, Player 2 (between 1 & 4)? "))
            player += 1

    else:
        if (sticks_taken > pile) or (sticks_taken > 4) or (sticks_taken < 1):
            sticks_taken = int(raw_input("Please enter a legal value (1-4): "))
        else:
            pile -= sticks_taken
            print "There are", pile, "sticks left."
            if pile == 0:
                break
            sticks_taken = int(raw_input("How many sticks do you want to take, Player 1 (between 1 & 4)? "))
            player -= 1

if player == 1:
    print "Congradulations, Player 1. You won!"
else:
    print "Congradulations, Player 2. You won!"

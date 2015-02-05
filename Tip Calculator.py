# This program finds the total of a restaraunt bill 

total_bill = float(raw_input("What is the total bill? ")) 

total_bill_fifteen = float(total_bill + (total_bill * 0.15))
                   
total_bill_twenty = float(total_bill + (total_bill * 0.20))

print "The bill with 15% tip is $" + str(total_bill_fifteen)
                      
print "The bill with 20% tip is $" + str(total_bill_twenty) 

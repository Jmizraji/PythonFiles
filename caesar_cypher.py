# This program does a simple rotational encryption

user_text = raw_input("Please type a word that you would like to be encrypted: ").lower()
user_number = int(raw_input("Please type a number for the key: "))


integer_tuple = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")

cypher_text = ()
for i in user_text:
    value = integer_tuple.index(i)+user_number
    if value > 26:
        value = value - 26
        cypher_text += integer_tuple[value],
    else:
        cypher_text += integer_tuple[integer_tuple.index(i) + user_number],
print "".join(cypher_text)
        
        
    

    
    
    

import cPickle,shelve

nested=["first", ("second","third"),["fourth","fifth","sixth"]]
#print nested

scores=[("Moe", 1000),("Larry",1500),("Curly",3000)]
#print scores


#High Scores 2.0
#Demonstrates nested sequences
pickle_file=open("scores.dat","w+")
                  

#scores=[]

choice=None
while choice!="0":

    print\
    """
    High Scores Keeper

    0 - Quit
    1 - List Scores
    2 - Add a Score
    """

    choice=raw_input("Choice: ")
    print
    #exit
    if choice == "0":
        print "Good-bye."

#display high-score table:
    elif choice== "1":
        print "High Scores\n"
        print "NAME\tSCORE"
        for entry in scores:
            score,name = entry
            print name, "\t", score

#add a score
    elif choice == "2":
        name=raw_input("What is the player's name?: ")
        score=int(raw_input("What score did the player get?: "))
        entry=(name, score)
        scores.append(entry)
        scores.sort()
        scores.reverse()        #want the highest number first
        scores=scores[:5]       #keep only top 5 scores

#some unknown choice
    else:
        print "Sorry, but",choice,"isn't a valid choice."

cPickle.dump(scores,pickle_file)
pickle_file.close()
raw_input("\n\nPress the enter key to exit.")


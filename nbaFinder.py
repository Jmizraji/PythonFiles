import urllib,re,webbrowser

#create a function to test for a valid home page
def open_page(page):
    try:
        web_page = urllib.urlopen(page)
        #always use .read() in conjunction with RE
        lines = web_page.read()
        #some pages will return this....
        #it's not a valid page
        if "404 Page Not Found" in lines:
            print "Invalid Page(404) "
        web_page.close()
        #print lines
    except:
            print "Error opening that URL!"
            lines = []
    #return the text on the page
    return lines

#list all of the teams in the NBA
def team_list(pg_txt):
    #some teams have three words handled with [ ]?[\w]*?
    #the darn 76ers (real nba team at 13-47???),Anyway...the numbers that are in their name must be accounted for
    #[\d]*?to catch this exception where a team has numbers in name
    teams = re.findall('bi">[\w]*[ ][\d]*?[\w]*[ ]?[\w]*?', pg_txt)
    
    #Remove the bi>" from each team name...
    #bi only included to match the pattern, now we should remove it
    teams= [team[4:] for team in teams]
    #print clean_teams
    return teams



def team_links(pg_txt, team_list):
    #locates all the links on the page
    rel_links = re.findall('<a href="[?\w=/<> |]*"',pg_txt)
    #edit the links (the'll all be relative at this point
    #split at the quotes and retain item[1] = the link
    rel_links = [item.split("\"")[1] for item in rel_links]

    #this part is tricky, don't get too caught up on this
    #each team needs links grouped by their team...
    #links 0-3 match up with item[0] in the teams list
    #4-7 match up with item[1]....etc
    #we want to group all of each teams links into their own sublist
    #so that team_list[i] corresponds to the list of links [i]
    #where the list of links [i] will return all of the teams links
    start = 0
    stop = 3
    pair_list= []
    for team in team_list:
        sublist= []
        for i in range(int(start),int(stop)): 
            sublist.append(rel_links[i])
        #incriment start and stop to coordinate with the teams to change which links are added
        start+=4
        stop+=4
        #append the sublists to the master list
        pair_list.append(sublist)

    #print pair_list
            
    return pair_list

#takes a list of lists (org_list) which has all of a teams links grouped together.
def link_matcher(org_list, team_list):
    
    while True:
        choice = ""
        while choice.title() not in team_list:
            for team in team_list:
                print team,'\n'
            choice = raw_input('Please choose a valid NBA team^^ or Q to quit: ').title()

            #provide a way out of the loop
            if choice.upper() == 'Q':
                return "thanks for using this program!\n"

            
        print 'Great, we will open pages about',choice,'\n\n'
        #get the index of the choice....it'll correspond to the team which will correspond to it's links
        link_num= team_list.index(choice)
        valid_links = org_list[link_num]
        #print valid_links

        #figure out which page the user wants
        selection = raw_input('would you like to learn more about stats, schedule, or roster?\n>')

        #open the page of their choice
        if selection.lower() =='stats':
            webbrowser.open('http://www.espn.go.com'+valid_links[0])
        elif selection.lower() =='schedule':
            webbrowser.open('http://www.espn.go.com'+valid_links[1])
        elif selection.lower() == 'roster':
            webbrowser.open('http://www.espn.go.com'+valid_links[2])
        else:
            print 'bad choice'
		

        
    
#main
#load the data
home = 'http://www.espn.go.com/nba/teams'
page_text = open_page(home)
team_lister = team_list(page_text)
team_links_list = team_links(page_text,team_lister)

#this is where the user will decide what they want to open
link_matcher(team_links_list,team_lister)

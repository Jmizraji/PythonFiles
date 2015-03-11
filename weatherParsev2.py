#Weather Getter

#!/usr/bin/python
#^line needed for any script we want to run on server...
#place this file in your cgi-pub,
#use unix commands:
#chmod ugo+rx filename
#^^gives permissions to file name
#python filename
#^runs file
#chmod ugo+rx outputfilename.html
#^gives universal view privilages to the out put file
#view your output html file at cgi.soic.indiana.edu/~YOURUSERNAMEHERE/outputfilename.html


#tools for url reading, parsing, etc.
import urllib



def get_temps(page):
    #create a list to return and hold all weather data for each location
    parts_list = []

    #open the page
    web_page = urllib.urlopen(page)

    #readlines of page
    lines = web_page.readlines()

    #close the webpage
    web_page.close()

    #loop through each line so we can clean the data
    for line in lines:

        #swap the direction of all the tags
        #split at the tags in order to further separate the data btw tags
        parts = line.replace(">", "<").split("<")

        #loop through each item in parts
        #search for the &deg;f because the temp information will follow
        for item in parts:

            if 'id=\"divStationName' in item:
                parts_list.append(parts[4])
            elif "&deg;F" in item:
                #append the item that containts the degree info into the list
                parts_list.append(item)
                
                
    #delete the first item in the list (parts_list[0] just = unit of temperature used)
    del parts_list[0]
    return parts_list
            


    

#main
links =['http://weather.weatherbug.com/IN/Evansville-weather.html?zcode=z6286','http://weather.weatherbug.com/CA/Beverly%20Hills-weather.html?zcode=z6286&zip=90210'\
        ,'http://weather.weatherbug.com/NY/New%20York-weather.html?zcode=z6286','http://weather.weatherbug.com/IN/Bloomington-weather.html?zcode=z6286'\
        ,'http://weather.weatherbug.com/PA/Lavelle-weather.html?zcode=z6286&zip=17943','http://weather.weatherbug.com/IL/Chicago-weather.html?zcode=z6286']
#evansville, Oakland, NY, btown, lavelle, chicago
#add any weather bug links you want location information for here

#temp_list = get_temps('http://weather.weatherbug.com/IN/Evansville-weather.html?zcode=z6286')

#create a list to hold all of the lists of info
#a list of lips?! sounds like a table to me (rows = each sublist)
all_weather= []

#for each link
for link in links:
    #generate a list of temps using the function
    temp_list = get_temps(link)
    #add that list to overall list
    all_weather.append(temp_list)
    #location, current temp, hi,lo, wind_chill, dew point
#print all_weather

html= """
<table border
='1'>
<tr>
<th>Location</th><th>Current Temperature</th><th>Hi</th><th>Lo</th><th>Wind Chill</th><th>dew point</th>
</tr>
"""
for row in all_weather:
    html+= '<tr>'
    for data in row:
        html+= '<td>'
        html+= data
        html+= '</td>'
    html+= '</tr>'

html+= '</table>'
print html
out = open('weatherbug.html','w')
out.write(html)
out.close()

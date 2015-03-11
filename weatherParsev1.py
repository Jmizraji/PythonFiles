#WEather Parse

import urllib

baseurl = "http://www.crh.noaa.gov/ind/?mystation="
loci = ["KBMG","KAID","KBAK","KIND","KMIE"]
#bloomington, ander, cold, indy, muncie

all_data = []

for loc in loci:
    web_page = urllib.urlopen(baseurl+loc)
    lines = web_page.readlines()
    web_page.close()
    temps = [line.strip().replace(">","<").split("<") for line in lines if \
             "deg;" in line]
    print temps
    tempF = [item[6] for item in temps]
    tempC = [item[12] for item in temps]

    #print tempC,tempF

    location = [line.strip().replace(">","<").split('<') for line in lines if '/nobr' in \
                line and 'IN' in line]
    #print location
    location = [item[4] for item in location]
    print location
    data = (location,tempC,tempF)
    all_data.append(data)

#print all_data

html_text="""
<html><body>
<table border='1'><tr>
<th> Location</th><th> Temp C<th> <th> Temp F </th><tr>

"""

write_file = open("weather.html","w")
for entry in all_data: #refers to a whole row of data(tuple)
    html_text += "<tr>"
    for item in entry:
        html_text+="<td>"
        html_text += str(item)
        html_text+="</td>"
    html_text+="</tr>"

html_text+="""
</table></body>
</html>
"""




write_file.write(html_text)
write_file.close() 

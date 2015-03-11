import urllib, random, webbrowser
def link_list(page):
    web_page = urllib.urlopen(page)
    lines = web_page.readlines()
    web_page.close()
    links = []
    for line in lines:
    	parts = line.replace(">", "<").split("<")
    	for item in parts:
        	if "href" in item and "wiki" in item and ".org" not in item:
            	item = item[item.index("href="):]
            	link_parts = item.split("\"")
            	if len(link_parts) > 1:
                	links.append(link_parts[1])
    return links

#main
pages = [raw_input("Where would you like to start? ")]
current = pages[0]
jumps = int(raw_input("How many jumps? "))
webbrowser.open(current)
for i in range(jumps):
    print "Jumping from :", current
    pages = link_list(current)
    current = "http://en.wikipedia.org" + random.choice(pages)
    print "To :", current, "\n"
    webbrowser.open_new_tab(current)

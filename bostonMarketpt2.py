import urllib, csv
def find_zip_info(code):
	zip_codes = open("zipcode.csv", "r")
	read = csv.DictReader(zip_codes)
	for item in read:
    	if item["zip"] == code:
        	zip_codes.close()
        	return item
    	
	zip_codes.close()
	return False
def locations(b_url):
	web_page = urllib.urlopen(b_url)
	lines = web_page.readlines()
	web_page.close()
	print "Location Info:\n"
	for line in lines:
    	parts = line.replace(">", "<").split("<")
    	for item in parts:
        	if "Boston Market - " in item and "title" in item:
            	print item.split("Boston Market - ")[1].replace("\"", ""), "\t\t",
        	elif "miles" in item:
           	print item


#main
result = find_zip_info(raw_input("Please enter a zip code: "))
if result:
    baseurl = "http://m.bostonmarket.com/boston-market/locations?q={0}&type=manual"
    url = baseurl.format(result["latitude"] + " " + result["longitude"])
    print "Retrieved from:", url, "\n"
    locations(url)
else:
    print "Not a valid US Zip code!"

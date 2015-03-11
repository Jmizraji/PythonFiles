#Boston Market Pt1

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
result = find_zip_info(raw_input("Please enter a zip code: "))
if result:
    baseurl = "http://m.bostonmarket.com/boston-market/locations?q={0}&type=manual"
	url = baseurl.format(result["latitude"] + " " + result["longitude"])
	print url
else:
    print "Not a valid US Zip code!"

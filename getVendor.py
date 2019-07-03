#!/usr/bin/python
import requests
import sys


def getVendorName():
    API_KEY = "at_YhkZqmwmx3aPTNi6djBO8WGMXCc9g"

    MAC_ADDR = sys.argv[1]
    URL = "https://api.macaddress.io/v1?apiKey=" +API_KEY+ "&output=json&search=" + MAC_ADDR
    r = requests.get(url = URL)
    data = r.json()
    if data['vendorDetails']['companyName'].strip():
        print ("Vendor details for MAC Address "+MAC_ADDR+" : " + data['vendorDetails']['companyName'])
    else:
        print ("Vendor details not Found for MAC Address " + MAC_ADDR)

if __name__ == '__main__':
getVendorName()

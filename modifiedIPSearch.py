# This program will ask the user to give an IP and then validate if it is a private or public IP

import re, ipaddress, pandas, requests, os, json
import tkinter as tk
from tkinter import filedialog
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
print(API_KEY)
base_url = "https://api.abuseipdb.com/api/v2/check"

    
# This section prompts the user to select a file to parse for IPs

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

# This section parses the csv data for IPs

print("Parsing data...")

df = pandas.read_csv(file_path, dtype="object")
df2 = df
content = df2.iloc[:, 1:7].to_string()


print("Extracting IPs...")

# This section is the regex string used to detect IP addresses that are passed to the "ipcheck" variable, it uses the findall method against the ipcheck vairable and stores it in the match vairable

ip = re.compile(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
match = ip.findall(content)

print("Cleaning up duplicates...")

undupedmatch = []

for ipaddresses in match:
    if ipaddresses not in undupedmatch:
        undupedmatch.append(ipaddresses)
    else:
        continue

#This section determines if the IP address found is a public or private IP address, we only want public IPs

public = []

print("Checking Database...")

try:
    for validaddresses in undupedmatch:
        if ipaddress.IPv4Address(validaddresses).is_global == True:
            public.append(validaddresses)
        else:
            continue
except ipaddress.AddressValueError:
    pass

addresses = public

for address in addresses:
   url = (f"{base_url}/{address}")

   querystring = {
    "ipAddress": str(address)
}

   headers = {
    "Accept": "application/json",
    "Key": str(API_KEY)
}

   response = requests.request(method="GET", url=base_url, headers=headers, params=querystring)

   decodedResponse = json.loads(response.text)
   print(decodedResponse)

if response.status_code == 200:
    pass
else:
    print(f"Failed to retrieve data {response.status_code}")


# Current issues: if pulled IP is private, it does not get stored in address and therefore causes NameError for some reason

# Need to discard duplicate IPs

# Need to do proper JSON parsing so that only the IP address, confidence score, domain, total reports and country code are returned 

# Would like to have it prompt the user to enter their API key in which it would store it temporarily until the program closes (or just have the user add a .env file in the folder with their API key)




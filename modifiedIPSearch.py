# This program will ask the user to give an IP and then validate if it is a private or public IP

import re, ipaddress
import tkinter as tk
from tkinter import filedialog

# This section prompts the user to select a file to parse for IPs

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

with open(file_path, encoding="UTF-8") as file_path:
    content = file_path.read()


# This section is the regex string used to detect IP addresses that are passed to the "ipcheck" variable, it uses the findall method against the ipcheck vairable and stores it in the match vairable
ip = re.compile(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")

match = ip.findall(content)

#This section determines if the IP address found is a public or private IP address, we only want public IPs

public = []

for x in match:
    if ipaddress.IPv4Address(x).is_global == True:
        public.append(x)
    else:
        continue

print("These are all of the public IPs found " + str(public))

# Need to implement dialog box for file selection

# Need to pull data from imported csv, store in a variable and then do the above loop on it

# Need to take those pulled IPs and store them in a seperate variable

# Need to loop through that variable performing an API call on each loop to AbuseIPDB

# On each API call need to determine if there are malicious indicators and then determine what to do with detections (store in a file, print to screen, store in a var and do something else)


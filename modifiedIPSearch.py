# This program will ask the user to give an IP and then validate if it is a private or public IP

import re, ipaddress

# This section is the regex string used to detect IP addresses that are passed to the "ipcheck" variable, it uses the findall method against the ipcheck vairable and stores it in the match vairable
ip = re.compile(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
ipcheck = input("Enter an IP Address to check: ") 
match = ip.findall(ipcheck)

#This section determines if the IP address found is a public or private IP address, we only want public IPs

public = []

for x in match:
    if ipaddress.IPv4Address(x).is_global == True:
        public.append(x)
    else:
        continue

print("These are all of the public IPs found " + str(public))

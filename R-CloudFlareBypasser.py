import socket, sys, os

# Print banner
print(''' ___                    ___            _____
| _ \\___ _ __  __ ___ _| _ ) _____ __ |_   _|__ __ _ _ __
|   / -_) '  \\/ _` \\ \\ / _ \\/ _ \\ \\ /   | |/ -_) _` | '  \\
|_|_\\___|_|_|_\\__,_/_\\_\\___/\\___/_\\_\\   |_|\\___\\__,_|_|_|_|
CloudFlare bypasser , Get Real IP of website
Created By Maximum Radikali, modified by GramThanos
''')

domain = input("Please Enter a url ex : (google.com)-> ")

try:
  hostname = socket.gethostbyname(domain)
  print('The public hostname is: ' + hostname + ' (' + domain + ')')
except:
  print('Failed to get the public hostname for ' + domain)

subdomains = open("dom.txt","r")
print("Checking subdomains ...")

found = 0
for subdomain in subdomains:
  subdomain = subdomain.strip()
  try:
    hostname = socket.gethostbyname(subdomain + domain)
    print('Found posible hostname: ' + hostname + ' (' + subdomain + domain + ')')
    found += 1
  except:
    pass
if found > 0:
  print ("The operation has been successful :)")
else:
  print ("The operation has been unsuccessfully :(")

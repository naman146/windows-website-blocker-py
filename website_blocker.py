"""this program is to block a website from being open for a particular period of time
You can edit it according to your needs and timings
Just schedule this code as an administrator in windows under windows task scheduler,
so that it can run at startup evrytime your pc gets started"""

import time
from datetime import datetime as dt

#path for host file
#host_path='C:\Windows\System32\drivers\etc'
# I am using a copied file of that host file
host_path = 'hosts'
redirect = "127.0.0.1"
website_list = ['www.facebook.com','facebook.com']

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 1) < dt.now() < dt(dt.now().year
          , dt.now().month, dt.now().day, 2):
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    
    else:
        with open(host_path , 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for cont in content:
                if not any(website in cont for website in website_list):
                    file.write(cont)
            file.truncate()
    
    time.sleep(300)
     
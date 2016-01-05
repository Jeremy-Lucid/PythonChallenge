import urllib

if __name__ == "__main__":
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    passcode = "63579" #"8022" #"12345"
    while(1 > 0):
        url1 = url + passcode
        f = urllib.urlopen(url1)# -*- coding: utf-8 -*-
        passcode = f.read()
        print passcode
        passcode = passcode.split()[-1]


# when the code is 16044, it said divided by two and keep going
# so here I stop the program, restart from 16044/2


#and the next nothing is 82682
#There maybe misleading numbers in the 
#text. One example is 82683. Look only for the next nothing and the next nothing is 63579
#and the next nothing is 37278


#peak.html

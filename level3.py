# author: Haoyu Qi
# date: 12/25/2015

import requests
from bs4 import BeautifulSoup,Comment
from level2 import decode

def case(l):
    """return 1 if its uppercase, return 0 if its lowercase"""
    if l == '!': 
        return 0
    else:
        return int(l.isupper())
    
#text = "aBCDeFGHijk"

def trans(ls):
    """transfer a list of chars to a list of binaries"""
    return map(case, ls)
    
if __name__ == "__main__":
    #read data
    url = "http://www.pythonchallenge.com/pc/def/equality.html"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    text = str(comments[0])
    text = decode(text, delete = "\n")
    text = '!' + text + '!'
    
    #process
    for i in range(4, len(text)-4):
        if case(text[i]) == 0:
            around = text[i-4:i+5] # get three letters on the left, three on the right
            #print around
            bi_str = trans(around) #transfer to biniary
            if bi_str == [0,1,1,1,0,1,1,1,0]:
                print text[i]
                
    #anwser:
    #linkedlist    
  

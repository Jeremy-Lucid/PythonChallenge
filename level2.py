# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup,Comment

import string
def decode(m ,delete = ''):
    """Input a string of encoded message, out put the decoded one"""
    frm = ''
    to =  ''
    table = string.maketrans(frm,to)
    md = m.translate(table, delete)
    return md
    
if __name__ == "__main__":
    
    url = "http://www.pythonchallenge.com/pc/def/ocr.html"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    print comments[0]
    message = str(comments[1])
    print decode(message, delete = "%$@()_!+&^{}#[]*\n")
    #answer
    #equality
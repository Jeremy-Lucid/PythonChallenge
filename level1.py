# -*- coding: utf-8 -*-
# to decode the message, we need to right shift each letter by two

#def decode(l):
#    """input a letter l, output the one right shiftted
#    
#        l: char
#    """
#    a = ord('a')
#    z = ord('z')
#    numlet = z -a +1
#    if l.isalpha():
#        asci = ord(l)-a  #get the ASCII code for letter l
#        asci = (asci + 2) % numlet
#        lc = chr(a + asci)
#    else:
#        lc = l
#    return lc
import string
def decode(m):
    """Input a string of encoded message, out put the decoded one"""
    frm = 'abcdefghijklmnopqrstuvwxyz'
    to =  'cdefghijklmnopqrstuvwxyzab'
    table = string.maketrans(frm,to)
    md = m.translate(table)
    return md
    
    
if __name__ == '__main__':
    message = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp." +\
    "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle." +\
    " sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print decode(message)
    answer = "map"
    print decode(answer)
    
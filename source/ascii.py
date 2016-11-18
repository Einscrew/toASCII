#!/usr/bin/python

import sys #doing nothing right now

def text(txt):  #073 068 126
    i = 0
    c = 0
    buffer = ''
    output = ''
    while i < len(txt):
        c = 0
        while c < 3:
            buffer = buffer + txt[i+c]
            c += 1
        output = output + chr(int(buffer))
        buffer = ''
        i+=4
    return output

def ascii(txt): #blahblahblah
    i = 0
    output = ''
    while i < len(txt):
        output = output + str(getAscii(txt[i]))
        i+=1
    return output

def getAscii(character):
    if len(str(ord(character))) < 3:
        return '0' + str(ord(character)) + ' '
    else:
        return str(ord(character)) + ' '

def main():
    answer = input('Press:\t[other to quit]\n1-to Ascii\t2-to Text\n')
    while(answer == 1 or answer == 2):
        if answer == 1:
            print ascii(str(raw_input('Insert the text:\n')))
        if answer == 2:
            print text(str(raw_input('Insert ASCII code:\n')))
        answer = input('\n\nPress:\n1-to Ascii\t2-to Text\n')
    return 0

main()

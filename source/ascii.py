#!/usr/bin/python

import sys #doing nothing right now

def ascii(txt):  #073 068 126
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
    print output

ascii(str(raw_input('Insira em ASCII:\n')))

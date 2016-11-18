from ascii import *

def main():
    answer = input('Press:\t[other to quit]\n1-to Ascii\t2-to Text\n')
    while(answer == 1 or answer == 2):
        if answer == 1:
            print ascii(str(raw_input('Insert the text:\n')))
        if answer == 2:
            print text(str(raw_input('Insert ASCII code:\n')))
        answer = input('\n\nPress:\t[other to quit]\n1-to Ascii\t2-to Text\n')
    return 0

main()

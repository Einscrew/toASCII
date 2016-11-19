from ascii import *

template = 'Result:---->  '
nValInput = 'Not a valid input'
def main():

    inp = None
    try:
        answer = input('Press:\t[other to quit]\n1-to Ascii\t2-to Text\n')
    except SyntaxError:
        answer = None
        print 'Not a valid input'

    while(answer == 1 or answer == 2):
        if answer == 1:
            try:
                inp = str(raw_input('Insert the text:\n'))
            except:
                print nValInput
            print template + ascii(inp)
        if answer == 2:
            try:
                inp = str(raw_input('Insert ASCII code:\n'))
            except:
                print nValInput
            print template + text(inp)

        try:
            answer = input('\n\nPress:\t[other to quit]\n1-to Ascii\t2-to Text\n')
        except SyntaxError:
            answer = None
            print nValInput
    return 0

main()

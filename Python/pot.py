'''Pot

    William Ikenna-Nwosu (wiknwo)

    The teacher has sent an e-mail to her students with 
    the following task: “Write a program that will 
    determine and output the value of X if given the 
    statement:

    X = number1^pow1 + number2^pow2 + … + numberN^powN
'''
def main():
    n = int(input(""))
    addends = []
    total = 0
    for i in range(n):
        addend = input("")
        valuestring = ''
        power = 0
        for j in range(0, len(addend) - 1):
            valuestring = valuestring + addend[j]
        valuestring = int(valuestring)
        power = int(addend[len(addend) - 1])
        total += valuestring**power
    print(total)
        
if __name__ == '__main__':
    main()
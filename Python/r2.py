'''R2

    William Ikenna-Nwosu (wiknwo)

    The number S is called the mean of two numbers R1 and 
    R2 if S is equal to (R1+R2)/2. Mirko’s birthday present 
    for Slavko was two integers R1 and R2. Slavko promptly 
    calculated their mean which also happened to be an 
    integer but then lost R2! Help Slavko restore R2.

    Input
    The first and only line of input contains two integers 
    R1 and S, both between −1000 and 1000.

    Output
    Output R2 on a single line.
'''
def main():
    data = input("").split(' ')
    r1 = int(data[0])
    s = int(data[1]) # mean
    r2 = (2 * s) - r1
    print(r2)

if __name__ == '__main__':
    main()


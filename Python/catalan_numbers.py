'''Catalan Numbers

    William Ikenna-Nwosu (wiknwo)

    Input
    The first line of input consists of an integer q, where 
    1≤q≤1000. Then follow q lines, each containing an 
    integer x where 1≤x≤5000.

    Output
    Then for each query x, output a line containing Cx, the 
    x:th Catalan number.
'''
from math import comb

def catalan_number(x):
    '''Function to calculate the xth catalan number

        Args:
            x(int): x

        Raises:

        Return:
            c_x(int): c_x
    '''
    return int((1 / (x + 1)) * comb(2 * x, x))

def main():
    q = int(input(""))
    for i in range(q):
        x = int(input(""))
        print(catalan_number(x))

if __name__ == '__main__':
    main()
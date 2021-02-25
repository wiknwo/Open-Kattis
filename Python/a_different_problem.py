'''A Different Problem

    William Ikenna-Nwosu (wiknwo)

    Write a program that computes the difference between 
    non-negative integers.

    Input
    Each line of the input consists of a pair of integers. 
    Each integer is between 0 and 1015 (inclusive). The 
    input is terminated by end of file.

    Output
    For each pair of integers in the input, output one 
    line, containing the absolute value of their 
    difference.
'''
import sys
def main():
    for line in sys.stdin:
        data = line.split(" ")
        data = list(map(int, data))
        print(abs(data[0] - data[1]))
        # Ctrl + z to signify EOF

if __name__ == '__main__':
    main()




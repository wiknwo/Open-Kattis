'''Zamka

    William Ikenna-Nwosu (wiknwo)

    The impossible has happened. Bear G. has fallen into 
    his own trap. Lured by a delicious box of Domaćica, 
    without even thinking, he rushed and fell into his 
    trap. In order to get out of the trap, he must solve 
    the following task with your help. You are given 
    three integers L, D and X.

    determine the minimal integer N such that L≤N≤D and 
    the sum of its digits is X

    determine the maximal integer M such that L≤M≤D and 
    the sum of its digits is X

    Input
    The first line of input contains the integer 
    L (1≤L≤10000), the number from the task. The second 
    line of input contains the integer D (1≤D≤10000, L≤D), 
    the number from the task. The third line of input 
    contains the integer X (1≤X≤36), the number from the 
    task.

    Output
    The first line of output must contain the integer N 
    from the task. The second line of output must 
    contain the integer M from the task.
'''
def sum_digits(number):
    str_number = str(number)
    running_sum = 0
    for char in str_number:
        if char.isdigit():
            running_sum += int(char)
    return running_sum

def main():
    l = int(input(""))
    d = int(input(""))
    x = int(input(""))
    n = 11000 # minimal integer such that sum(digits) = X
    m = -1 # maximal integer such that sum(digits) = X

    for i in range(l, d + 1):
        if i < n and sum_digits(i) == x:
            n = i
        if i > m and sum_digits(i) == x:
            m = i
    print(n)
    print(m)
if __name__ == '__main__':
    main()
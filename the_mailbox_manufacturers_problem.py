'''The Mailbox Manufacturers Problem

    wiknwo

    In the good old days when Swedish children were still 
    allowed to blow up their fingers with fire-crackers, 
    gangs of excited kids would plague certain smaller 
    cities during Easter time, with only one thing in mind: 
    To blow things up. Small boxes were easy to blow up, 
    and thus mailboxes became a popular target. Now, a 
    small mailbox manufacturer is interested in how many 
    fire-crackers his new mailbox prototype can withstand 
    without exploding and has hired you to help him. He will 
    provide you with k (1≤k≤10) identical mailbox prototypes 
    each fitting up to m (1≤m≤100) crackers.

    However, he is not sure of how many fire-crackers he 
    needs to provide you with in order for you to be able to 
    solve his problem, so he asks you. You think for a while 
    and then say:

    “Well, if I blow up a mailbox I can’t use it again, so 
    if you would provide me with only k=1 mailboxes, I 
    would have to start testing with 1 cracker, then 2 
    crackers, and so on until it finally exploded. In the 
    worst case, that is if it does not blow up even when 
    filled with m crackers, I would need 1+2+3+…+m=m(m+1)2 
    crackers. If m=100 that would mean more than 5000 fire-
    crackers!”

    “That’s too many”, he replies. “What if I give you more 
    than k=1 mailboxes? Can you find a strategy that 
    requires fewer fire crackers?”

    Can you? And what is the minimum number of crackers 
    that you should ask him to provide you with?

    You may assume the following:

    - If a mailbox can withstand x fire-crackers, it can 
    also withstand x−1 fire-crackers.

    - Upon an explosion, a mailbox is either totally 
    destroyed (blown up) or unharmed, which means that 
    it can be reused in another test explosion.

    Note: If the mailbox can withstand a full load of m 
    fire-crackers, then the manufacturer will of course 
    be satisfied with that answer. But otherwise he is 
    looking for the maximum number of crackers that his 
    mailboxes can withstand.

    Input
    The input starts with a single integer N (1≤N≤100) 
    indicating the number of test cases to follow. Each 
    test case is described by a line containing two 
    integers: k and m, separated by a single space.

    Output
    For each test case print one line with a single integer 
    indicating the minimum number of fire-crackers that is 
    needed, in the worst case, in order to figure out how 
    many crackers the mailbox prototype can withstand.
'''
import sys

# 0 <= k <= 11, 0 <= start, end <= 100
memo = [[[0 for z in range(101)] for j in range(101)] for i in range(11)]

def solve(k, start, end):
    #print("k: {}, start: {}, end: {}".format(k, start, end))
    if k == 0:
        return sys.maxsize

    if k == 1:
        return (end * (end + 1) / 2) - (start * (start + 1) / 2)

    if end <= start:
        return 0
    if memo[k][start][end] == 0:
        result = sys.maxsize
        for c in range(start + 1, end + 1):
            result = min(result, c + max(solve(k - 1, start, c - 1), solve(k, c, end)))
        memo[k][start][end] = result
    return memo[k][start][end]

def main():
    n = int(input(""))
    data = []

    for i in range(n):
        data.append(input("").split(" "))
        k = int(data[i][0])
        m = int(data[i][1])
        print(int(solve(k, 0, m)))

if __name__ == '__main__':
    main()
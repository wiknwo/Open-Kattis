'''Help a PhD Candidate Out!

    William Ikenna-Nwosu (wiknwo)

    Jon Marius forgot how to add two numbers while doing 
    research for his PhD. And now he has a long list of 
    addition problems that he needs to solve, in addition 
    to his computer science ones! Can you help him?

    On his current list Jon Marius has two kinds of 
    problems: addition problems on the form “a+b” and the 
    ever returning problem “P=NP”. Jon Marius is a quite 
    distracted person, so he might have to solve this last 
    problem several times, since he keeps forgetting the 
    solution. Also, he would like to solve these problems 
    by himself, so you should skip these.

    Input
    The first line of input will be a single 
    integer N (1≤N≤1000) denoting the number of testcases. 
    Then follow N lines with either “P=NP” or an addition 
    problem on the form “a+b”, where a,b∈[0,1000] are 
    integers.

    Output
    Output the result of each addition. For lines 
    containing “P=NP”, output “skipped”.
'''
def main():
    n = int(input(""))

    for i in range(n):
        problemstr = input("")
        if '+' in problemstr:
            plus_index = problemstr.find('+')
            first_number = problemstr[:plus_index]
            first_number = int(first_number)
            second_number = problemstr[plus_index + 1:]
            second_number = int(second_number)
            print(first_number + second_number)
        else:
            print('skipped')
if __name__ == '__main__':
    main()
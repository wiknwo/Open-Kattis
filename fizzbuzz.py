'''FizzBuzz

    William Ikenna-Nwosu (wiknwo)

    According to Wikipedia, FizzBuzz is a group word 
    game for children to teach them about division. This 
    may or may not be true, but this question is generally 
    used to torture screen young computer science 
    graduates during programming interviews.

    Basically, this is how it works: you print the 
    integers from 1 to N, replacing any of them divisible 
    by X with Fizz or, if they are divisible by Y, with 
    Buzz. If the number is divisible by both X and Y, you 
    print FizzBuzz instead.

    Input
    Input contains a single test case. Each test case 
    contains three integers on a single line, X, Y and N 
    (1≤X<Y≤N≤100).

    Output
    Print integers from 1 to N in order, each on its own 
    line, replacing the ones divisible by X with Fizz, 
    the ones divisible by Y with Buzz and ones divisible 
    by both X and Y with Fizz
'''
def main():
    data = input("").split(" ")
    data = list(map(int, data))
    x = data[0]
    y = data[1]
    n = data[2]

    for i in range(1, n + 1):
        if i % x == 0 and i % y == 0:
            print("FizzBuzz")
        elif i % x == 0:
            print("Fizz")
        elif i % y == 0:
            print("Buzz") 
        else:
            print(i)

if __name__ == '__main__':
    main()
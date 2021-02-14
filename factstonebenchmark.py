'''Factstone Benchmark

    William Ikenna-Nwosu (wiknwo)

    Amtel has announced that it will release a 128-bit 
    computer chip by 2010, a 256-bit computer by 2020, 
    and so on, continuing its strategy of doubling the 
    word-size every ten years. (Amtel released a 64-bit 
    computer in 2000, a 32-bit computer in 1990, a 
    16-bit computer in 1980, an 8-bit computer in 1970, 
    and a 4-bit computer, its first, in 1960.)

    Amtel will use a new benchmark – the Factstone – to 
    advertise the vastly improved capacity of its new 
    chips. The Factstone rating is defined to be the 
    largest integer n such that n! can be 
    represented as an unsigned integer in a computer word.
    Given a year 1960≤y≤2160, what will be the Factstone 
    rating of Amtel’s most recently released chip?

    Input
    There are several test cases. For each test case, 
    there is one line of input containing y. A line 
    containing 0 follows the last test case.

    Output
    For each test case, output a line giving the 
    Factstone rating.
'''
import math
def rounddown(x):
    return int(math.floor(x / 10.0)) * 10

def main():
    while True:
        y = int(input(""))
        if y == 0:
            break

        # year_bits = {1960:4, 1970:8, 1980:16, 1990:32, 2000:64,
        #             2010:128, 2020:256, 2030:512, 2040: 1024,
        #             2050:2048, 2060:4096, 2070:8192, 2080:16384}
        year_bits = {}
                    
        for i, year in enumerate(range(1960, 2170, 10)):
            year_bits[year] = 2**(i + 2)
                    
        y = rounddown(y)
        bits = year_bits[y]

        # factstone = 0
        # while math.factorial(factstone) <= 2**bits:
        #     factstone += 1
        years_to_n = {}
        running_sum, n, year = 0, 2, 1960
        while year < 2170:
            running_sum += math.log2(n)
            if running_sum > year_bits[year]:
                years_to_n[year] = n - 1
                year += 10
            n += 1
        print(years_to_n[rounddown(y)])
        print(years_to_n)

        # print(factstone - 1)

if __name__ == '__main__':
    main()
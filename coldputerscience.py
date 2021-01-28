'''Cold-puter Science

    William Ikenna-Nwosu (wiknwo)

    We’re not going to sugar-coat it: Chicago’s winters 
    can be rough. The temperatures sometimes dip to 
    uncomfortable levels and, after last year’s “polar 
    vortex”, the University of Chicago Weather Service 
    wants to find out exactly how bad the winter was. 
    More specifically, they are interested in knowing the 
    total number of days in which the temperature was 
    below zero degrees Celsius.

    Input
    The input is composed of two lines. The first line 
    contains a single positive integer n (1≤n≤100) that 
    specifies the number of temperatures collected by the 
    University of Chicago Weather Service. The second line 
    contains n temperatures, each separated by a single 
    space. Each temperature is represented by an integer 
    t (−1000000≤t≤1000000)

    Output
    You must print a single integer: the number of 
    temperatures strictly less than zero.
'''
def main():
    number_of_temperatures = input("")
    temperatures = input("").split(" ")
    temperatures = list(map(int, temperatures))
    number_of_temperatures_less_zero = 0

    for temperature in temperatures:
        if temperature < 0:
            number_of_temperatures_less_zero += 1
    print(number_of_temperatures_less_zero)

if __name__ == '__main__':
    main()



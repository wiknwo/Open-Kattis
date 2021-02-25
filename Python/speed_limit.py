'''Speed Limit

    William Ikenna-Nwosu (wiknwo)

    ill and Ted are taking a road trip. But the odometer 
    in their car is broken, so they don’t know how many 
    miles they have driven. Fortunately, Bill has a working 
    stopwatch, so they can record their speed and the total 
    time they have driven. Unfortunately, their record 
    keeping strategy is a little odd, so they need help 
    computing the total distance driven. You are to write a 
    program to do this computation.

    this means they drove 2 hours at 20 miles per hour, 
    then 6−2=4 hours at 30 miles per hour, then 7−6=1 hour 
    at 10 miles per hour. The distance driven is then 
    2⋅20+4⋅30+1⋅10=40+120+10=170 miles. Note that the total 
    elapsed time is always since the beginning of the trip, 
    not since the previous entry in their log.

    Input
    The input consists of one or more data sets (at most 10). 
    Each set starts with a line containing an integer n, 
    1≤n≤10, followed by n pairs of values, one pair per line. 
    The first value in a pair, s, is the speed in miles per 
    hour and the second value, t, is the total elapsed time. 
    Both s and t are integers, 1≤s≤90 and 1≤t≤12. The values 
    for t are always in strictly increasing order. A value 
    of −1 for n signals the end of the input.

    Output
    For each input set, print the distance driven, followed 
    by a space, followed by the word “miles”.
'''
def main():
    time_at_speed = 0
    total_distance = 0
    previous_t = 0

    while True:
        n = int(input(""))
        if n == -1:
            break
        for i in range(n):
            data = input("").split(" ")
            data = list(map(int, data))
            s = data[0] # Speed in miles/hour
            t = data[1] # time in hours
            time_at_speed = t - previous_t
            previous_t = t
            total_distance += s * time_at_speed
        print("{} miles".format(total_distance))
        previous_t = 0
        total_distance = 0

if __name__ == '__main__':
    main()
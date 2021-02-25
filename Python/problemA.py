'''Problem A

    William Ikenna-Nwosu (wiknwo)

    You have produced a list of all the n upcoming requests 
    specified in milliseconds. Whenever a request comes in, 
    it will immediately be sent to one of your servers. A 
    request will take exactly 1000 milliseconds to process, 
    and it must be processed right away.

    Each server can work on at most k requests 
    simultaneously. Given this limitation, can you 
    calculate the minimum number of servers needed to 
    prevent another system breakdown?

    Input
    The first line contains two integers 1≤n≤100 000 and 
    1≤k≤100 000, the number of upcoming requests and the 
    maximum number of requests per second that each server 
    can handle.

    Then follow n lines with one integer 0≤ti≤100 000 each, 
    specifying that the ith request will happen ti 
    milliseconds from the exact moment you notified your 
    customers. The timestamps are sorted in chronological 
    order. It is possible that several requests come in at 
    the same time.

    Output
    Output a single integer on a single line: the minimum 
    number of servers required to process all the incoming 
    requests, without another system breakdown.
'''
def main():
    # Getting user input
    data = input("").split(" ")
    timestamps = [] # i th request will happen t_i milliseconds from the exact moment you notified your customers. 
    n = int(data[0]) # number of upcoming requests
    k = int(data[1]) # maximum number of requests per second that each server can handle
    for i in range(n):
        timestamps.append(int(input("")))
    
    # Calculating number of required servers
    min_num_servers = 0
    server = []
    flag = True # Flag to check 
    for i in range(len(timestamps) - 1):
        if abs(timestamps[i] - timestamps[i + 1]) < 1000:
            server.append(timestamps[i])
            flag = False
    if flag:
        min_num_servers = 1
        print(min_num_servers)
    elif not flag:
        print(len(server))
if __name__ == '__main__':
    main()
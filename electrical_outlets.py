'''Electrical Outlets

    William Ikenna-Nwosu (wikwno)

    Roy has just moved into a new apartment. Well, 
    actually the apartment itself is not very new, even 
    dating back to the days before people had electricity 
    in their houses. Because of this, Roy’s apartment has 
    only one single wall outlet, so Roy can only power one 
    of his electrical appliances at a time.

    Roy likes to watch TV as he works on his computer, and 
    to listen to his HiFi system (on high volume) while he 
    vacuums, so using just the single outlet is not an 
    option. Actually, he wants to have all his appliances 
    connected to a powered outlet, all the time. 
    The answer, of course, is power strips, and Roy has 
    some old ones that he used in his old apartment. 
    However, that apartment had many more wall outlets, 
    so he is not sure whether his power strips will 
    provide him with enough outlets now.

    Your task is to help Roy compute how many appliances 
    he can provide with electricity, given a set of power 
    strips. Note that without any power strips, Roy can 
    power one single appliance through the wall outlet. 
    Also, remember that a power strip has to be powered 
    itself to be of any use.
'''
def main():
    # Getting user input
    n = int(input(""))
    for i in range(n):
        data = input("").split(" ")
        k = int(data[0])
        outlets_in_power_strip = list(map(int, data[1:]))
        # print('k: {}, outlets in power strip {}'.format(k, outlets_in_power_strip))

        # Calculating maximum number of appliances that can be powered
        max_num_appliances_powered = 0

        if k == 1:
            max_num_appliances_powered = outlets_in_power_strip[0]
        else:
            for j in range(k - 1):
                max_num_appliances_powered += outlets_in_power_strip[j] - 1
            max_num_appliances_powered += outlets_in_power_strip[k - 1]
        print(max_num_appliances_powered)
if __name__ == '__main__':
    main()
'''Zabe

    William Ikenna-Nwosu (wiknwo)

    The Frog Regent has arranged his N frog servants in a 
    circle, with each frog facing the back of the next one. 
    Each frog is assigned a unique integer identifier (ID) 
    from the set of 1 to N. The frog arrangement is 
    specified as a sequence of IDs. The sequence always 
    starts with the frog with the ID 1. It is followed by 
    the ID of the frog in front of it, then the ID of the 
    next one, and so on until the ID of the last frog – 
    the one behind the frog with ID 1.

    A frog is considered to have made a single leap if it 
    has jumped over the frog in front of it, swapping 
    places with it in the process. For example, if the 
    frogs are sequenced as “1 5 4 3 2 6” and the frog with 
    ID 2 makes two leaps, the resulting sequence will be 
    “1 2 5 4 3 6” (the frog has shifted two places forward). 
    When the Frog Regent proclaims the number B, the frog 
    with ID B makes B leaps.

    The Frog Regent wishes, using some number of 
    proclamations, to rearrange the frogs from the 
    starting sequence to his favourite resulting sequence. 
    Given the starting and resulting frog sequences, write 
    a program that will compute a sequence of proclamations 
    needed for the Regent to rearrange the frogs into the 
    resulting sequence. Naturally, the starting and 
    resulting sequences will not be equal.

    Input
    The first line of input contains a positive integer N, 
    the number of frogs (3≤N≤100).

    The second line of input contains a permutation of the 
    first N positive integers, the starting frog sequence.

    The third line of input contains another permutation of 
    the first N positive integers, the resulting frog 
    sequence.

    Output
    Output any sequence of integers (one integer per line) 
    that the Frog Regent can proclaim in order to rearrange 
    the frogs into the resulting sequence.

    The number of proclamations must not exceed 100000.

    The test data will be such that a solution exists.
'''
def proclamation(number, frog_servants):
    '''Function to shift frog 'number', number places in the frog servants circle

        Args:
            number(int): number
            frog_servants(list): frogservants
        
        Raises:

        Return:
            void
    '''
    index = frog_servants.index(number)
    frog_servants.remove(number)
    frog_servants.insert((index + number) % len(frog_servants), number)
    return number

def main():
    # Get user input
    n = input("")
    starting_frog_sequence = input("").split(" ") 
    starting_frog_sequence = list(map(int, starting_frog_sequence))
    resulting_frog_sequence = input("").split(" ")
    resulting_frog_sequence = list(map(int, resulting_frog_sequence))
    
    # Fill in frogservants circle
    frogservants = []
    for frog in starting_frog_sequence:
        frogservants.append(frog)
    
    # Make proclamations until current sequences = resulting sequence
    count = 0
    while frogservants != resulting_frog_sequence and count <= 100000:  
        for i in range(1, len(frogservants) + 1):
            if resulting_frog_sequence[i - 1] != frogservants[i - 1]:
                print(proclamation(i, frogservants))
                count = count + 1

if __name__ == '__main__':
    main()
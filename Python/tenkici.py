'''Tenkici

    William Ikenna-Nwosu (wiknwo)

    Mirko found a collection of N toy tanks dating back 
    to the Second World War on his grandfather’s attic. 
    He promptly called his friend Slavko to play with him. 
    They made a battlefield – a wooden board consisting of 
    squares in N rows and N columns.

    Each tank can be moved to one of the four neighbouring 
    squares in a single move. A tank can shoot at any 
    square in the same row and column. The tank is said to 
    be guarding the row and column it is in.

    Additionally, no two tanks can be in the same square 
    at any time.

    After many hours of play and two previous attempts, 
    Mirko’s mom yelled at them to come down for lunch 
    again, and they decided to rearrange the tanks so that 
    each tank guards a different row and column 
    (meaning also that each row and column contains only 
    one tank).

    However, they want to do this using the minimum number 
    of moves.

    Write a program that finds the minimum number of 
    moves required to rearrange the tanks so that each 
    row and each column contains a single tank, and one 
    such shortest sequence of moves.
'''
def main():
    n = int(input("")) # Number of toy tanks
    data = []
    toy_tanks = []
    moves = 0

    for i in range(n):
        data = input("").split(' ')
        r = int(data[0])
        c = int(data[1])
        toy_tanks.append([r, c])

    # Moving tanks so that they are in separate rows and columns
    directions = ['L', 'R', 'U', 'D']

    # Check if a tank is in the same row
    for i in range(len(toy_tanks)):
        # Same row 
        if toy_tanks[i][0] == toy_tanks[j][0]:
            # Move down if possible
            if toy_tanks[i][0] < n:
                moves += 1
                toy_tanks[i][0] += 1
                print("{} D".format(i + 1))
            
            # Move up if possible
            if toy_tanks[i][0] > 1:
                moves += 1
                toy_tanks[i][0] -= 1
                print("{} U".format(i + 1))

        # Same column
        if toy_tanks[i][1] == toy_tanks[j][1]:
            # Move left if possible
            if toy_tanks[i][1] > 1:
                moves += 1
                toy_tanks[i][1] -= 1
                print("{} L".format(i + 1))

            # Move right if possible
            if toy_tanks[i][1] < n:
                moves += 1
                toy_tanks[i][1] += 1
                print("{} R".format(i + 1))




if __name__ == '__main__':
    main()
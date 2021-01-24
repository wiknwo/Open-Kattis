# William Ikenna-Nwosu (wiknwo)
# 
# Trivial: Parking
#
# When shopping on Long Street, Michael usually parks his 
# car at some random location, and then walks to the 
# stores he needs. Can you help Michael choose a place to 
# park which minimises the distance he needs to walk on 
# his shopping round?
#
# Long Street is a straight line, where all positions are 
# integer. You pay for parking in a specific slot, which 
# is an integer position on Long Street. Michael does not 
# want to pay for more than one parking though. He is very 
# strong, and does not mind carrying all the bags around.
def main():
    t = int(input("Enter number of test cases: "))
    longstreets = []
    
    # Get input from user
    for i in range(0, t):
        n = input("Enter number of stores: ")
        positions_on_longstreet = input("Enter position of stores on long street separated by space: ").split(" ")
        positions_on_longstreet = list(map(int, positions_on_longstreet))
        longstreets.append(positions_on_longstreet)
    print(longstreets)

    # Calculate minimum distance Michael walks and 
    # subtract first position from sum because that is 
    # where Michael parked
    minimum_walking_distance = 0         
    for i in range(0, len(longstreets)):
        longstreets[i].sort() # Sort positions in ascending order
        for j in range(1, len(longstreets[i])):
            minimum_walking_distance += (longstreets[i][j] - longstreets[i][j - 1])
        minimum_walking_distance += (longstreets[i][j] - longstreets[i][0])    
        print(minimum_walking_distance)
        minimum_walking_distance = 0
    
if __name__ == '__main__':
    main()
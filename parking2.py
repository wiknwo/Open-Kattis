# William Ikenna-Nwosu (wiknwo)
# 
# Parking https://open.kattis.com/problems/parking2
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
    t = int(input("")) # number of test cases

    for i in range(t):
        n = input("") # number of stores Michael wants to visit
        positions_on_longstreet = input("").split(" ")
        positions_on_longstreet = [int(x) for x in positions_on_longstreet]
        distance = max(positions_on_longstreet) - min(positions_on_longstreet)
        print(distance * 2)
    # t = int(input("")) # number of test cases
    
    # # Get input from user
    # for i in range(0, t):
    #     n = input("") # number of stores Michael wants to visit
    #     positions_on_longstreet = input("").split(" ")
    #     positions_on_longstreet = list(map(int, positions_on_longstreet))
    #     positions_on_longstreet.sort() # Sort the street

    #     # Calculate minimum distance Michael walks and 
    #     # subtract first position from sum because that is 
    #     # where Michael parked
    #     minimum_walking_distance = 0         
    #     for i in range(1, len(positions_on_longstreet)):
    #         minimum_walking_distance += (positions_on_longstreet[i] - positions_on_longstreet[i - 1])
    #     minimum_walking_distance += (positions_on_longstreet[i] - positions_on_longstreet[0])    
    #     print(minimum_walking_distance)
    #     minimum_walking_distance = 0
    
if __name__ == '__main__':
    main()
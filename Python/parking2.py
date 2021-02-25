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
        
if __name__ == '__main__':
    main()
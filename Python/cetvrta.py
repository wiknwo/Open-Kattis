'''Cetvrta

    William Ikenna-Nwosu (wiknwo)

    Mirko needs to choose four points in the plane so that 
    they form a rectangle with sides parallel to the axes. 
    He has already chosen three points and is confident 
    that he hasn’t made a mistake, but is having trouble 
    locating the last point. Help him.

    Input
    Each of the three points already chosen will be given 
    on a separate line. All coordinates will be integers 
    between 1 and 1000.

    Output
    Output the coordinates of the fourth vertex of the 
    rectangle.
'''
def main():
    data = []
    rectangle = []

    # Getting user input
    data.append(input("").split(" "))
    data.append(input("").split(" "))
    data.append(input("").split(" "))
    
    for datum in data:
        rectangle.append(list(map(int, datum)))
    data.clear() # All data has been processed now
    rectangle.append([None, None]) # Put in default value for now

    # Calculate fourth point
    if rectangle[0][0] == rectangle[1][0] or rectangle[0][0] == rectangle[2][0]:
        if rectangle[0][0] == rectangle[1][0]:
            rectangle[3][0] = rectangle[2][0]
        else:
            rectangle[3][0] = rectangle[1][0]
    else:
        rectangle[3][0] = rectangle[0][0]
    if rectangle[0][1] == rectangle[1][1] or rectangle[0][1] == rectangle[2][1]:
        if rectangle[0][1] == rectangle[1][1]:
            rectangle[3][1] = rectangle[2][1]
        else:
            rectangle[3][1] = rectangle[1][1]
    else:
        rectangle[3][1] = rectangle[0][1]

    print('{} {}'.format(rectangle[3][0], rectangle[3][1]))

if __name__ == '__main__':
    main()

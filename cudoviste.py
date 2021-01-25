# William Ikenna-Nwosu
#
# Easy: Cudoviste
#
#
def main():
    data = input("").split(" ")
    r = int(data[0])
    c = int(data[1])
    parkinglot = []
    number_of_parking_spaces = {0:0, 1:0, 2:0, 3:0, 4:0}

    for i in range(0, r):
        parkinglot.append(input(""))
 
    for i in range(0, r - 1):
        for j in range(0, c - 1):
            w = parkinglot[i][j]
            x = parkinglot[i][j + 1]
            y = parkinglot[i + 1][j]
            z = parkinglot[i + 1][j + 1]

            if w == '#' or x == '#' or y == '#' or z == '#':
                pass

            elif w == '.' and x == '.' and y == '.' and z == '.':
                number_of_parking_spaces[0] += 1

            elif (w == '.' and x == '.' and y == '.' and z == 'X') or (w == '.' and x == '.' and y == 'X' and z == '.') or (w == '.' and x == 'X' and y == '.' and z == '.') or (w == 'X' and x == '.' and y == '.' and z == '.'):
                number_of_parking_spaces[1] += 1

            elif (w == '.' and x == '.' and y == 'X' and z == 'X') or (w == '.' and x == 'X' and y == 'X' and z == '.') or (w == 'X' and x == 'X' and y == '.' and z == '.') or (w == 'X' and x == '.' and y == 'X' and z == '.') or (w == '.' and x == 'X' and y == '.' and z == 'X') or (w == 'X' and x == '.' and y == '.' and z == 'X'):
                number_of_parking_spaces[2] += 1

            elif (w == '.' and x == 'X' and y == 'X' and z == 'X') or (w == 'X' and x == 'X' and y == 'X' and z == '.') or (w == 'X' and x == 'X' and y == '.' and z == 'X') or (w == 'X' and x == '.' and y == 'X' and z == 'X'):
                number_of_parking_spaces[3] += 1

            elif (w == 'X' and x == 'X' and y == 'X' and z == 'X'):
                number_of_parking_spaces[4] += 1   

    for i in range(5):
        print(number_of_parking_spaces[i])

if __name__ == '__main__':
    main()
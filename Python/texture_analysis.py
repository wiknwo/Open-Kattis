'''Texture Analysis

    William Ikenna-Nwosu (wiknwo)
    
    determines if every pair of adjacent black pixels is 
    separated by the same number of white pixels
'''
def main():
    inputstr = ''
    textures = []
    period_count = 0
    period_counts = []
    test_cases = 1
    flag = True

    # Getting user input
    while inputstr != 'END':
        inputstr = input("")
        if inputstr != 'END':
            textures.append(inputstr)

    # Count number of periods between asterisk
    for texture in textures:
        for i in range(0, len(texture)):
            if texture[i] == '.':
                period_count += 1
            if texture[i] == '*' and i > 0:
                period_counts.append(period_count)
                period_count = 0
    
        for i in range(0, len(period_counts) - 1):
            if period_counts[i] != period_counts[i + 1]:
                flag = False
                break
        if flag:
            print("{} EVEN".format(test_cases))

        if not flag:
            print("{} NOT EVEN".format(test_cases))
        period_counts.clear()
        period_count = 0
        flag = True
        test_cases += 1

if __name__ == '__main__':
    main()
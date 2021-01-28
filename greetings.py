'''Greetings!

    William Ikenna-Nwosu (wiknwo)

    Now that Snapchat and Slingshot are soooo 2018, the 
    teenagers of the world have all switched to the new 
    hot app called BAPC (Bidirectional and Private 
    Communication). This app has some stricter social 
    rules than previous iterations. For example, if 
    someone says goodbye using Later!, the other person 
    is expected to reply with Alligator!. You can not 
    keep track of all these social conventions and 
    decide to automate any necessary responses, 
    starting with the most important one: the 
    greetings. When your conversational partner opens 
    with he…ey, you have to respond with hee…eey as 
    well, but using twice as many e’s!

    Given a string of the form he…ey of length at most 
    1000, print the greeting you will respond with, 
    containing twice as many e’s.
'''
def main():
    # Get user input
    inputstr = input("")
    e_count = 0
    outputstr = 'h'

    # Count the number of e's
    for char in inputstr:
        if char == 'e':
            e_count += 1

    # Print output string
    for i in range(e_count * 2):
        outputstr += 'e'
    outputstr += 'y'
    print(outputstr)

if __name__ == '__main__':
    main()
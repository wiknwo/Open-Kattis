'''Phone List

    William Ikenna-Nwosu (wiknwo)

    Given a list of phone numbers, determine if it is 
    consistent in the sense that no number is the 
    prefix of another. Let’s say the phone catalogue 
    listed these numbers:

    Emergency 911

    Alice 97 625 999

    Bob 91 12 54 26

    In this case, it’s not possible to call Bob, because 
    the central would direct your call to the emergency 
    line as soon as you had dialled the first three digits 
    of Bob’s phone number. So this list would not be 
    consistent.

    Input
    The first line of input gives a single integer, 1≤t≤40, 
    the number of test cases. Each test case starts with 
    n, the number of phone numbers, on a separate line, 
    1≤n≤10000. Then follows n lines with one unique phone 
    number on each line. A phone number is a sequence of 
    at most ten digits. Note that leading zeros in phone 
    numbers are significant, e.g., “0911” is a different 
    phone number than “911”

    Output
    For each test case, output “YES” if the list is 
    consistent, or “NO” otherwise.
'''
def main():
    t = int(input(""))

    for i in range(t):
        n = int(input(""))
        phone_numbers = []
        flag = True

        for j in range(n):
            phone_numbers.append(input(""))

        phone_numbers.sort()

        # Check if one phone number is a substring of another
        for j in range(1, len(phone_numbers)):
            if phone_numbers[j].startswith(phone_numbers[j - 1]):
                flag = False
                break

        phone_numbers.clear()

        if flag:
            print("YES")
        elif not flag:
            print("NO")
    
if __name__ == '__main__':
    main()

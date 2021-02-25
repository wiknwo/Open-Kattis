'''Frosh Week

    William Ikenna-Nwosu (wiknwo)

    During Frosh Week, students play various fun games to 
    get to know each other and compete against other teams. 
    In one such game, all the frosh on a team stand in a 
    line, and are then asked to arrange themselves 
    according to some criterion, such as their height, 
    their birth date, or their student number. This 
    rearrangement of the line must be accomplished only 
    by successively swapping pairs of consecutive students. 
    The team that finishes fastest wins. Thus, in order to 
    win, you would like to minimize the number of swaps 
    required.

    Input
    The first line of input contains one positive 
    integer n, the number of students on the team, which 
    will be no more than one million. The following n lines 
    each contain one integer between 1 and 10^9 (inclusive), 
    the student number of each student on the team. No 
    student number will appear more than once.

    Output
    Output a line containing the minimum number of swaps 
    required to arrange the students in increasing order 
    by student number.
'''
current_cost = 0 # Global variale to count how many swaps have taken place
def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
                global current_cost
                current_cost += len(L) - i
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def main():
    n = int(input(""))
    student_numbers = []
    for i in range(n):
        datum = int(input(""))
        student_numbers.append(datum)
    mergeSort(student_numbers)
    print(current_cost)
if __name__ == '__main__':
    main()
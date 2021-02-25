'''Pet

    William Ikenna-Nwosu (wiknwo)

    In the popular show “Dinner for Five”, five 
    contestants compete in preparing culinary delights. 
    Every evening one of them makes dinner and each of 
    other four then grades it on a scale from 1 to 5. 
    The number of points a contestant gets is equal to 
    the sum of grades they got. The winner of the show 
    is of course the contestant that gets the most points.

    Write a program that determines the winner and how 
    many points they got.

    Input
    Five lines, each containing 4 integers, the grades 
    a contestant got. The contestants are numbered 1 to 
    5 in the order in which their grades were given.

    Output
    Output on a single line the winner’s number and their 
    points, separated by a space. The input data will 
    guarantee that the solution is unique.
'''
def main():
    data = []

    # Get user input
    data.append(input("").split(" "))
    data.append(input("").split(" "))
    data.append(input("").split(" "))
    data.append(input("").split(" "))
    data.append(input("").split(" "))
    scores = []

    # Convert list of strings to list of int
    for datum in data:
        scores.append(list(map(int, datum)))
    data.clear()

    # Sum the scores and return the max index and max score
    max_score = -1
    max_index = -1
    for index, score in enumerate(scores):
        if sum(score) > max_score:
            max_score = sum(score)
            max_index = index + 1
    print('{} {}'.format(max_index, max_score))

if __name__ == '__main__':
    main()
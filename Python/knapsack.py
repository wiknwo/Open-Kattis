'''Knapsack

    William Ikenna-Nwosu (wiknwo)

    Implement a solution to the classic knapsack 
    problem. You are given a knapsack that can hold up 
    to a certain weight (its capacity), and several items 
    you may choose to put in the knapsack. Each item has 
    a weight and a value. Choose a subset of the items 
    (which could be all of them, or none of them) having 
    the greatest value that fit into the knapsack (i.e. 
    the sum of the weights of the items you choose must 
    be less than or equal to the knapsack capacity).

    Input
    The input consists of between 1 and 30 test cases. 
    Each test case begins with an integer 1≤C≤2000, 
    giving the capacity of the knapsack, and an 
    integer 1≤n≤2000, giving the number of objects. 
    Then follow n lines, each giving the value and 
    weight of the n objects. Both values and weights 
    are integers between 1 and 10000.

    Output
    For each test case, output a line containing the 
    number of items chosen, followed by a line 
    containing the indices of the chosen items (the first 
    item has index 0, the second index 1, and so on). The 
    indices can be given in any order.
'''
def knapsack(capacity, weights, values, n):
    # Base Case
    if n == 0 or capacity == 0:
        return 0
    
    # If weight of nth item is more than knapsack of 
    # capacity W, then this item cannot be included in the
    # optimal solution
    if weights[n - 1] > capacity:
        return knapsack(capacity, weights, values, n - 1)

    # Return the max of two cases:
    # (1) nth item included
    # (2) nth item not included
    else:
        return max(values[n - 1] + knapsack(capacity - weights[n - 1], weights, values, n - 1), knapsack(capacity, weights, values, n - 1))
def main():
    data = input("").split(" ")
    c = int(data[0])
    n = int(data[1])
    values = []
    weights = []
    for i in range(n):
        data = input("").split(" ")
        values.append(int(data[0]))
        weights.append(int(data[1]))

    print(knapsack(c, weights, values, n))
if __name__ == '__main__':
    main()
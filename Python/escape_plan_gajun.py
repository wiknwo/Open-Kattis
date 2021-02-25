import math
from ast import literal_eval


class Graph:
    def __init__(self, robots, holes):
        self.holes = holes
        self.robots = robots
        self.adjMatrix = [[0 for i in range(holes)] for j in range(robots)]

    def can_fill_hole(self, r, h):
        self.adjMatrix[r][h] = 1


def max_matching(g: Graph):
    matchR = [-1] * g.holes  # record which robot is assigned to which hole

    hole_count = 0
    for r in range(g.robots):
        visited = [False] * g.holes  # all holes initially not visited

        # check if robot can be in a hole
        if bipartite_match(g, r, matchR, visited):
            hole_count += 1

    return hole_count


def bipartite_match(g: Graph, r, matchR, visited):
    for h in range(g.holes):
        if g.adjMatrix[r][h] and visited[h] == False:

            visited[h] = True
            # check if robot assigned earlier and check for other candidates
            if matchR[h] == -1 or bipartite_match(g, matchR[h], matchR, visited):
                matchR[h] = r
                return True

    return False


def get_input_coords(num_of_coords):
    coordinates = []
    for _ in range(num_of_coords):
        xy_coord = [literal_eval(coord) for coord in input().split()]
        coordinates.append(xy_coord)

    return coordinates


def distance_equation(p1, p2):
    return math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))


######################
scenarios = 1
scenario_dict = dict()

while True:
    num_of_robots = int(input())
    if num_of_robots == 0:
        break
    robot_coords = get_input_coords(num_of_robots)
    num_of_holes = int(input())
    hole_coords = get_input_coords(num_of_holes)
    scenario_name = "Scenario {}".format(scenarios)
    scenario_dict[scenario_name] = {
        'num_of_robots': num_of_robots,
        'robot_coords': robot_coords,
        'num_of_holes': num_of_holes,
        'hole_coords': hole_coords
    }
    scenarios += 1

for name, d in scenario_dict.items():
    num_of_robots = d['num_of_robots']
    num_of_holes = d['num_of_holes']
    robot_coords = d['robot_coords']
    hole_coords = d['hole_coords']

    print(name)
    for second in [5, 10, 20]:
        distance = second * 10

        graph = Graph(num_of_robots, num_of_holes)
        for robot in range(num_of_robots):
            for hole in range(num_of_holes):
                if distance_equation(robot_coords[robot], hole_coords[hole]) <= distance:
                    graph.can_fill_hole(robot, hole)

        print("In {} seconds {} robot(s) can escape".format(second, max_matching(graph)))
    print()

"""
5
1.0 1.0
2.0 2.0
99.0 99.0
00.0 1000.0
3000.0 200.0
3
99.0 0.0
0.0 1000.0
1000.0 1000.0
3
0.0 0.0
10.0 0.0
0.0 10.0
3
99.0 0.0
0.0 1000.0
1000.0 1000.0
3
0.0 0.0
100.0 0.0
200.0 0.0
2
95.0 50.0
105.0 50.0
3
1.0 1.0
2.0 2.0
99.0 99.0
0
3
0.0 0.0
10.0 0.0
0.0 10.0
3
99.0 0.0
0.0 1000.0
1000.0 1000.0
3
0.0 0.0
100.0 0.0
200.0 0.0
2
95.0 50.0
105.0 50.0
0
"""
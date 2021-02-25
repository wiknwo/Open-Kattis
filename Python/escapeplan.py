# William Ikenna-Nwosu (wiknwo)
# 
# Hard: Escape Plan
# 
# You are a land surveyor, and you use the latest 
# land-surveying technology: robotic surveyors. You have 
# sent your robots to survey a remote field, since it is 
# cheaper and easier to send them than to go yourself. You 
# know that there are frequent sand storms that blow through 
# the field, which can damage the robots. Fortunately, 
# satellite imagery can detect these storms and give the 
# robots a warning several seconds before a storm arrives.
# 
# Since the field is so exposed and remote, the only way a 
# robot can protect itself is to run to a hole in the ground 
# and hide. You have identified the locations of several of 
# these holes, but each of them is large enough to fit only 
# one robot. Any robot that doesn’t make it into a hole before 
# the storm arrives will be damaged.
# 
# Write a program that will figure out how many robots can 
# escape a coming storm by running to and hiding in holes. 
# Assume that each robot that can escape travels from 
# its current position directly to a hole. All robots 
# travel at a speed of 10 meters per second.
from pprint import pprint
from collections import defaultdict
import math

def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def calculate_closest_hole(robots, holes):
    robots_closest_holes = {}
    distancesdict = {}
    for i in range(0, len(robots)):
        for j in range(0, len(holes)):
            distancesdict[j] = euclidean_distance(robots[i], holes[j])
        minimum_distance = min(distancesdict.values())

        # Get hole with minimum distance
        for key in distancesdict.keys():
            if distancesdict[key] == minimum_distance:
                robots_closest_holes[i] = key

    return robots_closest_holes

def move_robot(robot, time, hole):
    xreached = False
    yreached = False
    escaped = False
    for i in range(0, time):
        if robot[0] >= hole[0]:
            xreached = True
        if robot[1] >= hole[1]:
            yreached = True
        if xreached and yreached:
            escaped = True
            return robot
        if robot[0] < hole[0]:
            robot[0] = robot[0] + 10
        if robot[1] < hole[1]:
            robot[1] = robot[1] + 10 
    return escaped

def main():
    # File Processing
    path = 'C:\\Users\\willi\\Documents\\aCraft\\Open-Kattis\\escapeplan\\sample.in'
    data = [] # list to hold lines in file
    scenarios = [] # list to hold scenarios
    with open(path, 'r') as f:
        for line in f:
            data.append(line.rstrip())
   # print(data) # Check if data was read in correctly
    linenumber = 0 # Count which line in the file the data has been processed for
    numberofrobots = -1 # number of robots on the field

    # do while loop in python
    while True:
        numberofrobots = int(data[linenumber]) 
        linenumber = linenumber + 1

        # Leave loop when there are no more scenarios left
        if numberofrobots == 0:
            break

        # Getting robot coordinates
        robots = []
        for i in range(0, numberofrobots):
            coordinates = data[linenumber].split(" ")
            robots.append([float(coordinates[0]), float(coordinates[1])])
            linenumber = linenumber + 1

        numberofholes = int(data[linenumber])
        linenumber = linenumber + 1

        # Getting coordinates of holes
        holes = []
        for i in range(0, numberofholes):
            coordinates = data[linenumber].split(" ")
            holes.append([float(coordinates[0]), float(coordinates[1])])
            linenumber = linenumber + 1

        # Record scenario
        scenarios.append([robots, holes])

    # Compile output file
    path = 'C:\\Users\\willi\\Documents\\aCraft\\Open-Kattis\\escapeplan\\output.txt'
    outputfile = open(path, "w") # Open the file for writing
    for i in range(0, len(scenarios)):
        outputfile.write("Scenario {}\n".format(i + 1))
        escaped_robots_count = 0
        robots = scenarios[i][0] # Get robots for this scenario
        holes = scenarios[i][1]

        # Create boolean dict marking which holes have been entered by robots
        holesentered = {}
        for index in range(0, len(holes)):
            holesentered[index] = False

        times = [5, 10, 20] # Create list of time robot managed to escape in 5, 10 and 20 seconds   
        robot = robots[i] # Get the robots for scenario i
        for k in range(0, 3):
            for m in range(0, len(robots[i])):
                # Calculate closest hole for each robot
                robots_closest_holes = calculate_closest_hole(robots, holes)
                # Find positions of robots after times[k] seconds
                robot = robots[i]
                if move_robot(robot, times[k], holes[robots_closest_holes[i]]):
                    escaped_robots_count = escaped_robots_count + 1
                    holesentered[robots_closest_holes[i]] = True
                    del holesentered[robots_closest_holes[i]]
            # Write to output file
            outputfile.write("In {} seconds {} robot(s) can escape\n".format(times[k], escaped_robots_count))
            # Reset values
            escaped_robots_count = 0
            for index in range(0, len(holes)):
                holesentered[index] = False
        
        if i < len(scenarios) - 1:
            outputfile.write("\n")

if __name__ == '__main__':
    main()
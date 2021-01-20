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
        print(numberofrobots)

        # Getting robot coordinates
        robots = []
        for i in range(0, numberofrobots):
            coordinates = data[linenumber].split(" ")
            robots.append([float(coordinates[0]), float(coordinates[1])])
            linenumber = linenumber + 1
        print(robots)

        numberofholes = int(data[linenumber])
        linenumber = linenumber + 1

        # Getting coordinates of holes
        holes = []
        for i in range(0, numberofholes):
            coordinates = data[linenumber].split(" ")
            holes.append([float(coordinates[0]), float(coordinates[1])])
            linenumber = linenumber + 1
        #print(holes)

        # Record scenario
        scenarios.append([robots, holes])
    pprint(scenarios)

if __name__ == '__main__':
    main()
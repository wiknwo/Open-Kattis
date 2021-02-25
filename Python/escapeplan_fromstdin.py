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
    robot_to_move = robot
    xreached = False
    yreached = False
    holereached = False
    distance_between_robot_hole_x = abs(robot[0] - hole[0])
    distance_between_robot_hole_y = abs(robot[1] - hole[1])
    for i in range(0, time):
        if xreached and yreached:
            holereached = True
            #print("x and y reached")
            return holereached # Here

        if robot_to_move[0] == hole[0]:
            xreached = True
            #print("x reached")

        if distance_between_robot_hole_x < 10 and not xreached:
            if robot_to_move[0] - hole[0] < 0:
                robot_to_move[0] += distance_between_robot_hole_x
                if robot_to_move[0] == hole[0]:
                    # print(robot_to_move[0])
                    xreached = True
            elif robot_to_move[0] - hole[0] > 0:
                robot_to_move[0] -= distance_between_robot_hole_x
                if robot_to_move[0] == hole[0]:
                    # print(robot_to_move[0])
                    xreached = True
            #robot_to_move[0] += distance_between_robot_hole_x
            
            
        if robot_to_move[1] == hole[1]:
            yreached = True
            #print("yreached")

        if distance_between_robot_hole_y < 10 and not yreached:
            if robot_to_move[1] - hole[1] < 0:
                robot_to_move[1] += distance_between_robot_hole_y
                if robot_to_move[1] == hole[1]:
                    # print(robot_to_move[1])
                    yreached = True
            elif robot_to_move[1] - hole[1] > 0:
                robot_to_move[1] -= distance_between_robot_hole_y
                if robot_to_move[1] == hole[1]:
                    # print(robot_to_move[1])
                    yreached = True
            #robot_to_move[1] += distance_between_robot_hole_y
            
        if robot_to_move[0] < hole[0] and not xreached:
            robot_to_move[0] = robot_to_move[0] + 10
            distance_between_robot_hole_x = abs(robot_to_move[0] - hole[0])
            #print("Robot {} moved forward 10m in x direction".format(robot))
            
        elif robot_to_move[1] < hole[1] and not yreached:
            robot[1] = robot_to_move[1] + 10
            distance_between_robot_hole_y = abs(robot_to_move[1] - hole[1])
            #print("Robot {} moved up 10m in y direction".format(robot))
            
        elif robot_to_move[0] > hole[0] and not xreached:
            robot_to_move[0] = robot_to_move[0] - 10
            distance_between_robot_hole_x = abs(robot_to_move[0] - hole[0])
            #print("Robot {} moved back 10m in x direction".format(robot))
            
        elif robot_to_move[1] > hole[1] and not yreached:
            robot_to_move[1] = robot_to_move[1] - 10
            distance_between_robot_hole_y = abs(robot_to_move[1] - hole[1])
            #print("Robot {} moved down 10m in y direction".format(robot))
            
    return holereached
        
def main():
    # Reading data in from console
    scenarios = [] # list to hold scenarios
    numberofrobots = -1 # number of robots on the field

    # do while loop in python
    while True:
       # numberofrobots = int(input("Enter numer of robots: ")) 
        numberofrobots = int(input("")) 

        # Leave loop when there are no more scenarios left
        if numberofrobots == 0:
            break

        # Getting robot coordinates
        robots = []
        for i in range(0, numberofrobots):
            #coordinates = input("Enter coordinates of robot separated by space: ").split(" ")
            coordinates = input("").split(" ")
            robots.append([float(coordinates[0]), float(coordinates[1])])
        
        numberofholes = int(input(""))

        # Getting coordinates of holes
        holes = []
        for i in range(0, numberofholes):
            #coordinates = input("Enter coordinates of hole separated by space: ").split(" ")
            coordinates = input("").split(" ")
            holes.append([float(coordinates[0]), float(coordinates[1])])

        # Record scenario
        scenarios.append([robots, holes])

    # Compile output file
    for i in range(0, len(scenarios)):
        print("Scenario {}".format(i + 1))
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
                robot = robots[m] # Get robot
                if move_robot(robot, times[k], holes[robots_closest_holes[m]]) and (holesentered[robots_closest_holes[m]] == False):
                    escaped_robots_count = escaped_robots_count + 1
                    holesentered[robots_closest_holes[m]] = True
                    #print("Escaped robots count: {}".format(escaped_robots_count))
                    #print(holesentered)
                    #print("Robot new position: {}".format(robot))
                    #print("Robot {} managed to escape in {} seconds".format(robots[m], times[k]))
            # Write to output file
            print("In {} seconds {} robot(s) can escape".format(times[k], escaped_robots_count))
            # Reset values
            escaped_robots_count = 0
            for index in range(0, len(holes)):
                holesentered[index] = False
        
        if i < len(scenarios):
            print("")

if __name__ == '__main__':
    main()
import math

def rotate(dir, current, deg):
    if dir == "R":
        current = current + deg
        if current > 360:
            current = current - 360
        if current == 360:
            current = 0
    else:
        current = current - deg
        if current < 0:
            current = current + 360
        if current == 360:
            current = 0
    return current

def getPartOne(instructionlist):
    xcoord = 0
    ycoord = 0
    facing = 90 #FACINGS: 0 = N, 90 = E, 180 = S, 270 = W; START FACING EAST
    
    for instruction in instructionlist:
        if instruction[0] == "R" or instruction[0] == "L":
            facing = rotate(instruction[0], facing, int(instruction[1:]))
        else:
            if instruction[0] == "N" or (facing == 0 and instruction[0] == "F"):
                ycoord += int(instruction[1:])
            elif instruction[0] == "S" or (facing == 180 and instruction[0] == "F"):
                ycoord -= int(instruction[1:])
            elif instruction[0] == "E" or (facing == 90 and instruction[0] == "F"):
                xcoord += int(instruction[1:])
            elif instruction[0] == "W" or (facing == 270 and instruction[0] == "F"):
                xcoord -= int(instruction[1:])
    return (abs(xcoord) + abs(ycoord))

def getPartTwo(instructionlist):
    shipPos = [0, 0]
    waypoint = [10, 1]
    
    for instruction in instructionlist:
        relx = waypoint[0] - shipPos[0]
        rely = waypoint[1] - shipPos[1]
        if instruction[0] == "R" or instruction[0] == "L":
            if instruction[0] == "R":
                waypoint = rotateWP(-(int(instruction[1:])), shipPos, waypoint)
            else:
                waypoint = rotateWP(int(instruction[1:]), shipPos, waypoint)
        elif instruction[0] == "N":
            waypoint[1] += int(instruction[1:])
        elif instruction[0] == "S":
            waypoint[1] -= int(instruction[1:])
        elif instruction[0] == "E":
            waypoint[0] += int(instruction[1:])
        elif instruction[0] == "W":
            waypoint[0] -= int(instruction[1:])
        else:
            shipPos = [shipPos[0] + (relx * int(instruction[1:])), shipPos[1] + (rely * int(instruction[1:]))]
            waypoint = [relx + shipPos[0], rely + shipPos[1]]
    return (abs(shipPos[0]) + abs(shipPos[1]))
    

def rotateWP(angle, origin, waypoint):
	newx = origin[0]+math.cos(math.radians(angle))*(waypoint[0]-origin[0])-math.sin(math.radians(angle))*(waypoint[1]-origin[1])
	newy = origin[1]+math.sin(math.radians(angle))*(waypoint[0]-origin[0])+math.cos(math.radians(angle))*(waypoint[1]-origin[1])
	return [round(newx), round(newy)]

with open("day12input.txt") as f:
    rawcontent = f.readlines()

rawcontent = [x.strip("\n") for x in rawcontent]

print("The Manhattan distance for part 1 is: " + str(getPartOne(rawcontent)))
print("The Manhattan distance for part 2 is: " + str(getPartTwo(rawcontent)))
input()


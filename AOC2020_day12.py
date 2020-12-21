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

with open("day12input.txt") as f:
    rawcontent = f.readlines()

rawcontent = [x.strip("\n") for x in rawcontent]

print("The Manhattan distance is: " + str(getPartOne(rawcontent)))
input()


def getRowNum(rowstring):
    rowlist = []
    for i in range(0,128):
        rowlist.append(i)
    count = len(rowlist)
    for i in range(0, len(rowstring)):
        count = int(count/2)
        if rowstring[i] == "F":
            if len(rowlist) == 2:
                return rowlist[0]
            else:
                del rowlist[count:len(rowlist)]
                count = len(rowlist)
        if rowstring[i] == "B":
            if len(rowlist) == 2:
                return rowlist[1]
            else:
                del rowlist[0:count]
                count = len(rowlist)

def getColNum(colstring):
    collist = []
    for i in range(0,8):
        collist.append(i)
    count = len(collist)
    for i in range(0, len(colstring)):
        count = int(count/2)
        if colstring[i] == "L":
            if len(collist) == 2:
                return collist[0]
            else:
                del collist[count:len(collist)]
                count = len(collist)
        if colstring[i] == "R":
            if len(collist) == 2:
                return collist[1]
            else:
                del collist[0:count]
                count = len(collist)

def GetPartTwo(sortedlist):
    myseat = sortedlist[1] + 1
    for i in range(1, len(sortedlist)-1):
        if sortedlist[i + 1] == myseat:
            myseat += 1
        else:
            return myseat

with open('day5input.txt') as f:
    content = f.readlines()
    
content = [x.strip() for x in content]

allSeats = []
    
for i in range(0, len(content)):
    fullstring = content[i]
    row = getRowNum(fullstring[0:7])
    col = getColNum(fullstring[7:])
    seatnum = row * 8 + col
    allSeats.append(seatnum)
   
allSeats.sort()
print("The highest seat: " + str(allSeats[-1]))
print("My seat: " + str(GetPartTwo(allSeats)))
input()

def getSlope(testString, index):
    if testString[index] == '#':
        return True
    else:
        return False

with open('day3input.txt') as f:
    content = f.readlines()
    
content = [x.strip() for x in content]

treeCount1 = 0 #right 1, down 1
treeCount2 = 0 #right 3, down 1
treeCount3 = 0 #right 5, down 1
treeCount4 = 0 #right 7, down 1
treeCount5 = 0 #right 1, down 2
indextotest = 0

for i in range(0, len(content)):
    stringtotest = content[i]
    while indextotest > len(stringtotest)-1:
        stringtotest += stringtotest
    if getSlope(stringtotest, indextotest):
        treeCount1 += 1
    indextotest += 1

indextotest = 0
for i in range(0, len(content)):
    stringtotest = content[i]
    while indextotest > len(stringtotest)-1:
        stringtotest += stringtotest
    if getSlope(stringtotest, indextotest):
        treeCount2 += 1
    indextotest += 3

indextotest = 0
for i in range(0, len(content)):
    stringtotest = content[i]
    while indextotest > len(stringtotest)-1:
        stringtotest += stringtotest
    if getSlope(stringtotest, indextotest):
        treeCount3 += 1
    indextotest += 5

indextotest = 0
for i in range(0, len(content)):
    stringtotest = content[i]
    while indextotest > len(stringtotest)-1:
        stringtotest += stringtotest
    if getSlope(stringtotest, indextotest):
        treeCount4 += 1
    indextotest += 7

indextotest = 0
for i in range(0, len(content), 2):
    stringtotest = content[i]
    while indextotest > len(stringtotest)-1:
        stringtotest += stringtotest
    if getSlope(stringtotest, indextotest):
        treeCount5 += 1
    indextotest += 1

# for i in range(0, len(content)):
    # stringtotest = content[i]
    # while indextotest1 > len(stringtotest)-1:
        # stringtotest += stringtotest
    # if getSlope(stringtotest, indextotest1):
        # if indextotest1 % 1 == 0:
            # treeCount1 += 1
        # if indextotest1 % 3 == 0:
            # treeCount2 += 1
        # if indextotest1 % 5 == 0:
            # treeCount3 += 1
        # if indextotest1 % 7 == 0:
            # treeCount4 += 1
        # if i % 2 == 0:
            # treeCount5 += 1
    # indextotest1 += 1

print(str(treeCount1))
print(str(treeCount2))
print(str(treeCount3))
print(str(treeCount4))
print(str(treeCount5))

print(str(treeCount1 * treeCount2 * treeCount3 * treeCount4 * treeCount5))
input()
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
indextotest1 = 0
indextotest2 = 0
indextotest3 = 0
indextotest4 = 0
indextotest5 = 0

for i in range(0, len(content)):
    stringtotest = content[i]
    while indextotest4 > len(stringtotest)-1:
        stringtotest += stringtotest
    if getSlope(stringtotest, indextotest1):
        treeCount1 += 1
    if getSlope(stringtotest, indextotest2):
        treeCount2 += 1
    if getSlope(stringtotest, indextotest3):
        treeCount3 += 1
    if getSlope(stringtotest, indextotest4):
        treeCount4 += 1
    indextotest1 += 1
    indextotest2 += 3
    indextotest3 += 5
    indextotest4 += 7

for i in range(0, len(content), 2):
    stringtotest = content[i]
    while indextotest5 > len(stringtotest)-1:
        stringtotest += stringtotest
    if getSlope(stringtotest, indextotest5):
        treeCount5 += 1
    indextotest5 += 1

print(str(treeCount1))
print(str(treeCount2))
print(str(treeCount3))
print(str(treeCount4))
print(str(treeCount5))

print(str(treeCount1 * treeCount2 * treeCount3 * treeCount4 * treeCount5))
input()
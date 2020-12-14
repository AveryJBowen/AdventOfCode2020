def checknums(orig, check):
    return bool(set(orig).intersection(check))

def getSum(sumlist):
    sumlist.sort()
    return sumlist[0] + sumlist[-1]

def getPartOne(numberlist):
    for i in range(25, len(numberlist)):
        twentyfive = numberlist[i-25:i]
        checklist = []
        for j in range(0, len(twentyfive)):
            checklist.append(numberlist[i] - twentyfive[j])
        if not checknums(twentyfive, checklist):
            return numberlist[i]
                

def getPartTwo(numberlist, numtofind):
    for i in range(0, len(numberlist)-1):
        for j in range(i, len(numberlist)):
            if sum(numberlist[i:j]) == numtofind:
                return getSum(numberlist[i:j])
 
with open('day9input.txt') as f:
    rawcontent = f.readlines()

rawcontent = [x.strip("\n") for x in rawcontent]
rawcontent = [int(x) for x in rawcontent]

num = getPartOne(rawcontent)
num2 = getPartTwo(rawcontent, num)

print("The first number that is not the sum of any 2 of previous 25 numbers is: " + str(num))
print("The encryption weakness is: " + str(num2))
input()
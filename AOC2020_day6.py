def getPartOne(biglist):
    totalcount = 0
    for i in range(0, len(biglist)):
        biglist[i] = biglist[i].replace("\n", "")
    for i in range(0, len(biglist)):
        uniquecount = len(set(biglist[i]))
        totalcount += uniquecount
    return totalcount

def getAnswers(grouplist):
    groupcount = 0
    runningset = set(grouplist[0])
    if len(grouplist) > 1:
        for i in range(1, len(grouplist)):
            runningset = runningset.intersection(grouplist[i])
            groupcount = len(runningset)
    else:
        groupcount = len(runningset)
    return groupcount

def getPartTwo(biglist2):
    totalcount = 0
    for i in range(0, len(biglist2)):
        singlegroup = biglist2[i].split("\n")
        totalcount += getAnswers(singlegroup)
    return totalcount

with open('day6input.txt') as f:
    content = f.read().split("\n\n")

with open('day6input.txt') as f:
    content2 = f.read().split("\n\n")

print("Sum of questions to which anyone answered yes: " + str(getPartOne(content)))
print("Sum of questions to which everyone in group answered yes: " + str(getPartTwo(content2)))
input()
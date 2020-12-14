def checknums(orig, check):
    return bool(set(orig).intersection(check))

def getPartOne(numberlist):
    for i in range(25, len(numberlist)):
        twentyfive = numberlist[i-25:i]
        checklist = []
        for j in range(0, len(twentyfive)):
            checklist.append(numberlist[i] - twentyfive[j])
        if not checknums(twentyfive, checklist):
            return numberlist[i]
                

with open('day9input.txt') as f:
    rawcontent = f.readlines()

rawcontent = [x.strip("\n") for x in rawcontent]
rawcontent = [int(x) for x in rawcontent]

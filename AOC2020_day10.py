def getPartOne(numberlist):
    onecount = 0
    threecount = 0
    for i in range(0, len(numberlist)):
        if i == 0:
            if numberlist[i] - 0 == 1:
                onecount += 1
            elif numberlist[i] - 0 == 3:
                threecount += 1
        else:
            if numberlist[i] - numberlist[i-1] == 1:
                onecount += 1
            elif numberlist[i] - numberlist[i-1] == 3:
                threecount += 1
    threecount += 1 #FOR THE DEVICE
    return (onecount * threecount)

with open('day10input.txt') as f:
    rawcontent = f.readlines()

rawcontent = [x.strip("\n") for x in rawcontent]
rawcontent = [int(x) for x in rawcontent]
rawcontent.sort()

print(str(getPartOne(rawcontent)))
input()
def getPartOne(numberlist):
    onecount = 0
    threecount = 0
    for i in range(0, len(numberlist)):
        if numberlist[i] - numberlist[i-1] == 1:
            onecount += 1
        elif numberlist[i] - numberlist[i-1] == 3:
            threecount += 1
    return (onecount * threecount)

def getPartTwo(adapterdict):
    adaptercount = {}
    for adapter in adapterdict:
        for possible in adapterdict[adapter]:
            if possible not in adaptercount.keys():
                if adapter in adaptercount.keys():
                    adaptercount[possible] = adaptercount[adapter]
                else:
                    adaptercount[possible] = 1
            else:
                adaptercount[possible] = adaptercount[possible] + (adaptercount[adapter])
    return adaptercount[max(adaptercount)]

with open('day10input.txt') as f:
    rawcontent = f.readlines()

rawcontent = [x.strip("\n") for x in rawcontent]
rawcontent = [int(x) for x in rawcontent]
rawcontent.append(0) #for the outlet

rawcontent.sort()
rawcontent.append(rawcontent[-1] + 3) #for the device

adapterset = {}
for num in rawcontent:
    adapterset[num] = [num+1, num+2, num+3]

print(str(getPartOne(rawcontent)))
print(str(getPartTwo(adapterset)))
input()
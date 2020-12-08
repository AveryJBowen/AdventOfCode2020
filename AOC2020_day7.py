import re

def makeBagDict(somefile):
    with open(somefile) as f:
        rawcontent = f.readlines()
    rawcontent = [x.strip(".\n") for x in rawcontent]
    allBags = {}
    for i in range(0, len(rawcontent)):
        singlebag = re.sub(" bags?", "", rawcontent[i])
        bag1 = singlebag.split(" contain ")
        outerbag = bag1[0]
        innerbags = bag1[1].split(", ")
        innerbagdict = {}
        for j in range(0, len(innerbags)):
            innerbag = innerbags[j]
            if innerbag == "no other":
                innerbagquant = 0
                innerbagcolor = "None"
            else:
                innerbagquant = innerbag.split(" ", 1)[0]
                innerbagcolor = innerbag.split(" ", 1)[1]
            innerbagdict[innerbagcolor] = innerbagquant
        allBags[outerbag] = innerbagdict
    return allBags

def getinnercount(somedict, bagcolor, count):
    count = count
    for x in somedict:
        if bagcolor in somedict[x]:
            count += 1
        
    return count

allInput = makeBagDict('day7input.txt')
print(getinnercount(allInput, "shiny gold", 0))
input()


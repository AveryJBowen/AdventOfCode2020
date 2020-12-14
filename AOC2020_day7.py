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
            innerbagdict[innerbagcolor] = int(innerbagquant)
        allBags[outerbag] = innerbagdict
    return allBags

def getParentBagList(bagdict, searchbag):
    immediateParentList = []
    for x in bagdict:
        if searchbag in bagdict[x]:
            immediateParentList.append(x)
    return immediateParentList

def getParents(searchdict, masterParentList):
    if len(masterParentList) == 0:
        for parent in getParentBagList(searchdict, "shiny gold"):
            masterParentList.append(parent)
        getParents(searchdict, masterParentList)
    else:
        for bag in masterParentList:
            for parent in getParentBagList(searchdict, bag):
                if parent not in masterParentList:
                    masterParentList.append(parent)
    return masterParentList

# def getChildrenDict(bagdict, searchbag):
    # immediateChildren = bagdict[searchbag]
    # return immediateChildren

# def getChildrenCount(bagdict, masterChildDict, count):
    # if count == 0:
        # masterChildDict.update(getChildrenDict(bagdict, "shiny gold"))
        # count = len(masterChildDict)
        # getChildrenCount(bagdict, masterChildDict, count)
    # else:
        # for child in masterChildDict:
            # multiplier = masterChildDict[child]
            # masterChildDict.update(getChildrenDict(bagdict, child))
            # for bag in child:
                # levelcount = multiplier * masterChildDict[bag]
                # count += levelcount
    # return count

masterBagDict = makeBagDict('day7input.txt')
parentBagsList = []
#childBagDict = {}
print("Number of bags that can eventually contain a shiny gold bag: " + str(len(getParents(masterBagDict, parentBagsList))))
#print("Number of bags in each shiny gold bag: " + str(getChildrenCount(masterBagDict, childBagDict, 0)))
input()


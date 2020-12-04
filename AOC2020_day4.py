def getPartOne(passwordstring):
    passcontents = passwordstring.split(" ")
    hasCountry = False
    for x in passcontents:
        if "cid" in x:
            hasCountry = True
    if len(passcontents) == 8:
        return True
    elif len(passcontents) == 7 and not hasCountry:
        return True
    else:
        return False

with open('day4input.txt') as f:
    content = f.read().split("\n\n") #this at least gets everything from one passport into a single string

#need to replace any '\n' in each string with a space:
for i in range(0, len(content)):
    content[i] = content[i].replace("\n", " ")

validCount = 0

for i in range(0, len(content)):
    if getPartOne(content[i]):
        validCount += 1

print(validCount)
input()
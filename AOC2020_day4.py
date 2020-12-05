import re

def getPartOne(passportstring):
    passcontents = passportstring.split(" ")
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

def validate(passportinfo):
    height = False
    eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    categories = ["cid", "byr", "iyr", "eyr", "hcl", "ecl", "pid", "hgt"]
    passportinfo = passportinfo.replace(":", " ")
    passcontentlist = passportinfo.split(" ")
    byr = passcontentlist[passcontentlist.index("byr") + 1]
    iyr = passcontentlist[passcontentlist.index("iyr") + 1]
    eyr = passcontentlist[passcontentlist.index("eyr") + 1]
    hcl = passcontentlist[passcontentlist.index("hcl") + 1]
    ecl = passcontentlist[passcontentlist.index("ecl") + 1]
    pid = passcontentlist[passcontentlist.index("pid") + 1]
    hgt = passcontentlist[passcontentlist.index("hgt") + 1]
    if hgt[-1] == "m":
        height = "150cm" <= hgt <= "193cm"
    elif hgt[-1] == "n":
        height = "59in" <= hgt <= "76in"
    else:
        height = False
    if len(pid) > 9:
        return False
    if (height and ("1920" <= byr <= "2002") and ("2010" <= iyr <= "2020") and ("2020" <= eyr <= "2030") and (re.match("[0-9]{9}", pid)) and (re.match("^#[a-f0-9]{6}", hcl)) and (ecl in eyecolors)):
        return True
    else:
        return False

def getPartTwo(passportstring):
    if validate(passportstring):
        return True
    else:
        return False

with open('day4input.txt') as f:
    content = f.read().split("\n\n") #this at least gets everything from one passport into a single string

#need to replace any '\n' in each string with a space:
for i in range(0, len(content)):
    content[i] = content[i].replace("\n", " ")

validCount1 = 0
validCount2 = 0

for i in range(0, len(content)):
    if getPartOne(content[i]):
        validCount1 += 1
        if getPartTwo(content[i]):
            validCount2 += 1

print("There are " + str(validCount1) + " valid passports for part 1")
print("There are " + str(validCount2) + " valid passports for part 2")
input()
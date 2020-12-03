def getPartOne(minNum, maxNum, letter, password):
    count = password.count(letter)
    if count >= minNum and count <= maxNum:
        return True
    else:
        return False

def getPartTwo(lowPos, highPos, letter, password):
    ind1 = lowPos - 1
    ind2 = highPos - 1
    if password[ind1] == letter and password[ind2] == letter:
        return False
    elif password[ind1] == letter or password[ind2] == letter:
        return True
    else:
        return False


with open('day2input.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]
validPasswords1 = 0
validPasswords2 = 0
for i in range(0, len(content)):
    stringtoparse = content[i]
    testMin = int(stringtoparse.split("-")[0])
    testMax = int(stringtoparse.split("-")[1].split()[0])
    testLetter = stringtoparse.split()[1].strip(":")
    testPassword = stringtoparse.split()[2]
    if getPartOne(testMin, testMax, testLetter, testPassword):
        validPasswords1 += 1
    if getPartTwo(testMin, testMax, testLetter, testPassword):
        validPasswords2 += 1
    i += 1

print(validPasswords1)
print(validPasswords2)
input()
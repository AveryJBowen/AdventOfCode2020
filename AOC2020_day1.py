def getPartOne(num1, num2):
    print(num1 * num2)
    
def getPartTwo(num1, num2, num3):
    print(num1 * num2 * num3)

with open('day1nums.txt') as f:
    content = f.readlines()
    
content = [x.strip() for x in content]
for i in range(0, len(content)):
    content[i] = int(content[i])

content.sort()
for i in range(0, len(content)):
    number1 = content[i]
    tofind = 2020 - content[i]
    if tofind in content:
        getPartOne(number1, tofind)
    else:
        i += 1

for i in range(0, len(content)):
    number1 = content[i]
    for j in range(i+1, len(content)):
        number2 = content[j]
        sum1 = number1 + number2
        if sum1 < 2020:
            tofind = 2020 - sum1
        if tofind in content:
            getPartTwo(number1, number2, tofind)
            break
            
input()
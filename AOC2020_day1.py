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
part1Found = False
part2Found = False

while part1Found == False:
    for i in range(0, len(content)):
        number1 = content[i]
        tofind = 2020 - content[i]
        if tofind in content:
            part1Found = True
            getPartOne(number1, tofind)
            break
        else:
            i += 1
            
testNum = 0
while part2Found == False:
    for i in range(0, len(content)):
        number1 = content[i]
        for j in range(i+1, len(content)):
            number2 = content[j]
            sum1 = number1 + number2
            if sum1 < 2020:
                tofind = 2020 - sum1
                if tofind in content:
                    if testNum == number1 or testNum == number2 or testNum == tofind:
                        break                  
                    else:
                        part2Found = True                        
                        getPartTwo(number1, number2, tofind)
                        testNum = number1                       
input()
def count(numList: [int], num: int) -> int:
    count = 0
    for i in numList:
        if i == num:
            count += 1
    return count
    
def singNum(numList: [int]) -> int:
##    print(sorted(numList))
##    sorted(numList)
    count = 0
    baseNum = numList[0]
    for num in sorted(numList):
        if num == baseNum:
            count += 1
            continue
        elif num != baseNum:
            if count == 1:
                return baseNum
            count = 1
            baseNum = num
    return baseNum
    
##    for num in numList:
##        if count(numList, num) == 1:
##            return num
        
##    for num in numList:
##        if numList.count(num) == 1:
##            return num

##main
numList = [ 2, 2, 1, 1, 3]
print(singNum(numList))

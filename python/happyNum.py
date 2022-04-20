def sumSquareDigits(num: int) -> int:
    Sum = 0
    for i in str(num):
        Sum += int(i)**2
    return Sum

def isHappyNum(num: int, checkList: [int]) -> bool:
    count = 0
    print(num)
    newNum = sumSquareDigits(num)
    if newNum == 1:
        return True
    if checkList.count(newNum) > 0: ##could be for loop that stops right when it sees one
        return False
    else:
        checkList.append(newNum)
        return(isHappyNum(newNum, checkList))
            

##main
num = 4
checkList = [num]
print(isHappyNum(num, checkList))
        

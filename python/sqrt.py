def sqrt(num: int)->int:
    root = 0
    while root*root <= abs(num):
        root += 1
    root -= 1
    if num < 0:
        return (-1*root)
    return root

##main
num = 1
print(sqrt(num))

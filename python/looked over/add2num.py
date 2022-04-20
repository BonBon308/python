def lis2num(lis):
    num = ""
    for i in reversed(lis):
        num += str(i)
    return int(num)

def num2lis(num):
    temp = str(num)
    lis = []
    for i in reversed(temp):
        lis.append(int(i))
    return lis

l1 = [9,9,9,9,9]
l2 = [9,9]

print(num2lis((lis2num(l1) + lis2num(l2))))

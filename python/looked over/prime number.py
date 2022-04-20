def isPrime(num):
    if num <= 1:
        return False
    for i in range (3, num-1):
        if num % i == 0:
            return False
    return True

##main
InputArray = [10, 5, 7, 3, 2, 1, 0, -1, 89]
PrimeArray = []
for i in InputArray:
    if (isPrime(i) == True):
        PrimeArray.append(i)
SortedArray = sorted(PrimeArray)
print(SortedArray)

def primeFactors(num):
    primeFactorArray = []
    if num <= 1:
        return primeFactorArray
    i = 2
    while num != 1:
        if num % i == 0:
            primeFactorArray.append(i)
            num = num/i
            i = 2
        else:
            i += 1
    return primeFactorArray

##main
InputArray = [121, 5, 40, 1, 2, 3, 4, 89, 0 , -1]
PrimeArray = []
for i in InputArray:
    PrimeArray.append(primeFactors(i))
print(PrimeArray)

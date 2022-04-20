def divide(dividend: int, divisor: int) -> int:
    if divisor == 0:
        print("cannot divide by 0")
        return -1
    if dividend == 0:
        return 0
    quotient = 0
    absDividend = abs(dividend)
    absDivisor = abs(divisor)
    while absDividend >= absDivisor:
        absDividend -= absDivisor
        quotient +=1
    if ( dividend > 0 and divisor < 0  or  dividend < 0 and divisor > 0 ):
        return (-1 * quotient)
    return quotient

##main
dividend = -10
divisor = 2
print(divide(dividend, divisor))


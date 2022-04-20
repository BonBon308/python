def isPalindrome(num):
    if num < 0:
        return False
    obj = str(num)
    i = 0
    while i <= (len(obj)/2):
        if obj[i] != obj[len(obj)-1-i]:
            return False
        i += 1
    return True

x= 102201
print(isPalindrome(x))

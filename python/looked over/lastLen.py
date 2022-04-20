def lastLen(string: str, delimiter: str = " ") -> int:
    count = 0
    for char in reversed(string):
        if char == delimiter:
            break
        count += 1
    return count

##main
string = "hello;world"
print(lastLen(string, delimiter=","))

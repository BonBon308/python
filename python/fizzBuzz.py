def fizzBuzz(num: int):
    i = 1
    output = []
    while i < num+1:
        if i % 15 == 0:
            output.append("FizzBuzz")
        elif i % 5 == 0:
            output.append("Buzz")
        elif i % 3 == 0:
            output.append("Fizz")
        else:
            output.append(str(i))
        i += 1
    return output

##main
print(fizzBuzz(15))

def tenthLine(file: str) -> str:
    openedFile = open(file, 'r')
    lineNum = 1
    while lineNum <= 10:
        line = openedFile.readline()
        lineNum += 1
    return line
##main
print(tenthLine('tenthLine.txt'))

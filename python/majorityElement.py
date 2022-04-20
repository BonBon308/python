import math
def majorityElement(group: list) -> int:
    halfNumElements = math.trunc( len(group)/2 )
    for i in group:
        if group.count(i) >= halfNumElements:
            return i

##main
group = [2, 3, 2, 2, 1, 1, 1]
print(majorityElement(group))


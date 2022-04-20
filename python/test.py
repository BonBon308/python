##import glob
##glob.glob('*.py')
##class c:
##    counter = 5
##    def __init__(self):
##        self.data = [1,2]
##    
##x = c()
##print(x.data)
##x.counter = 1
##print(x.counter)
##del x.counter
##print(x.counter)
##def average(values):
##    """Computes the arithmetic mean of a list of numbers.
##
##    >>> print(average([20, 30, 70]))
##    40.0
##    """
##    return sum(values) / len(values)
##
##import doctest
##doctest.testmod()
class parent():
    def __init__(self):
        print("parent")
##    pass

class child(parent):
    def __init__(self):
        parent.__init__(self)
        print("child")

    def hello():
        print("hello")

childEX = child()
child

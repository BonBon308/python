class parent():
    def do_A(self):
        print('parent a')
        self.do_B()
    
    def do_B(self):
        print('parent B')

class child(parent):
    # def do_A(self):
    #     print('child a')    
    #     # super().do_A()

    def do_B(self):
        print('child B')

exChild = child()
exChild.do_A()
        
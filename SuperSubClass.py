class Base1(object):
    def __init__(self, delta):
        print("O delta é válido ou não?")
        self.delta = int(input("Entre com o valor de delta: "))

class Derived1(Base1):
    def __init__(self,delta):
        Base1.__init__(self,delta)

        print("Derived")

    def comparar(self):

        if (self.delta == 0):
            return False



class Derived2(Base1):
    def __init__(self, delta):
        Base1.__init__(self,delta)
        print("Derived")

    def comparar(self):
        if(self.delta > 0):
            return True



ob = Derived1()
ob2 = Derived2()
ob.comparar()

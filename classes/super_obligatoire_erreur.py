class Base:
    def __init__(self):
        print("Base init")

class A(Base):
    def __init__(self):
        Base.__init__(self)
        print("A init")

class B(Base):
    def __init__(self):
        Base.__init__(self)
        print("B init")

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("C init")
    
c = C()
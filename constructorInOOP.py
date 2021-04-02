class A:
    def __init__(self):
        print("init A")

    def feature1(self):
        print("Hi I am from A")


# If you want to use super class than remove the inheritance of c class.
# class B(A):
class B:
    def __init__(self):
        # super().__init__()
        print("init B")

    def feature1(self):
        print("Hi I am form B")


class C(A, B):

    # This super method will always prefer class A because MRO(Method Resolution Order).
    def __init__(self):
        super().__init__()
        print("init C")

    def feature2(self):
        print("Hi I am form C")


cl = C()
cl.feature1()

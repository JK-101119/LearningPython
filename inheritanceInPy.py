# # This is GrandParent class defined.
#
# class GrandParent:
#     def feature1(self):
#         print("Feature 1 is here!")
#
#     def feature2(self):
#         print("Feature 2 is here!")
#
#
# # Single level inheritance by Parent class.
#
#
# class Parent(GrandParent):
#     def feature3(self):
#         print("Feature 3 is here!")
#
#     def feature4(self):
#         print("Feature 4 is here!")
#
#
# # Multi level inheritance by Child1 class.
#
#
# class Child1(Parent):
#     def feature5(self):
#         print("Feature 5 is here!")
#
#     def feature6(self):
#         print("Feature 6 is here!")
#
#
# # Multiple level inheritance by Child2 class.
#
#
# class Child2(Parent):
#     def feature7(self):
#         print("Feature 7 is here!")
#
#     def feature8(self):
#         print("Feature 8 is here!")
#
#
# print('--------------------- GrandParent JI -----------------------')
# d = GrandParent()
# d.feature1()
# d.feature2()
#
# # Here Parent can access all the features of GrandParent class.
# print('--------------------- Parent -----------------------')
# p = Parent()
# p.feature1()
# p.feature2()
# p.feature3()
# p.feature4()
#
# # Here Child1 can access all the features of Parent class and GrandParent class also.
# print('--------------------- Child1 -----------------------')
# c1 = Child1()
# c1.feature1()
# c1.feature2()
# c1.feature3()
# c1.feature4()
# c1.feature5()
# c1.feature6()
#
# # Here Child2 can access all the features of Parent class and GrandParent class also.
# print('--------------------- Child2 -----------------------')
# c2 = Child2()
# c2.feature1()
# c2.feature2()
# c2.feature3()
# c2.feature4()
# c2.feature7()
# c2.feature8()


# ======================================================================================================

# Here we are going to use super keyword to access the properties of super class.


class A:
    def __init__(self):
        print("From A")

    def feature1(self):
        print("Feature A is here!")

# class B(A):


class B:
    def __init__(self):
        super().__init__()
        print("From B")

    def feature1(self):
        super().feature1()
        print("Feature B is here!")

# In the case of conflict the preference will always given to Right Hand class that is A.


class C(A, B):
    def __init__(self):
        super().__init__()
        print("From C")

    def feature1(self):
        super().feature1()
        print("Feature C is here!")

# x = B()
# x.feature1()


x = C()
x.feature1()

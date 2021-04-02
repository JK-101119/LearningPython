class A:
    def show(self):
        print("I am A")


# Here int the following example we are overriding the show() method of B class by A class.
class B(A):
    pass

    # def show(self):
    #     print("I am B")


x = B()
x.show()

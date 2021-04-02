# def gen():
#     yield 5
#     yield 4
#     yield 3
#     yield 2
#     yield 1
#
#
# g = gen()
# print(g)
# print(g.__next__())
# print(g.__next__())
#
# for i in g:
#     print(i)
# print("-----------------------------------------------------------------------")


def count():
    num = 1
    while num <= 10:
        sqrt = num*num
        num += 1
        yield sqrt
# We can create an object of iterator by using yield keyword that is generator..


c = count()
for i in count():
    print(i)

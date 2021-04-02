# nums = [1, 3, 5, 7]
# print(nums[0])
# Iterator always remember the last iteration value.
# ite = iter(nums)
# print(ite.__next__())
# print(next(ite))
#
# for i in nums:
#     print(i)
print("------------------------------------------------")


class firstTen:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


count = firstTen()
for i in count:
    print(i)

# def calculate(n, **kwargs):
# print(kwargs)


# n += kwargs["add"]
# n *= kwargs["multiply"]

# print(n)


# calculate(2, add=3, multiply=5)

class Car:

    def __int__(self, **kw):
        self.make = kw("make")
        self.model = kw("model")


my_car

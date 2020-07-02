class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Model : {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))


print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

print("*" * 10)

print(kenwood.on)
Kettle.switch_on(kenwood)
print(kenwood.on)
print("*" * 30)

kenwood.power = 1.5
print (kenwood.power)
# show classes

class LightBulb():
    """
    Models a light bulb
    using OOP in python
    """
    __my_list = []

    def __init__(self, a, b):
        self.state = False
        self.__my_list = [0,2,5]

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False



# create instance of the class

lightbulb_one = LightBulb(10, 20)

print(lightbulb_one)
# print('m_list=',lightbulb_one.__my_list)
# lightbulb_one.__my_list[0] = 1000
# print('m_list1=',lightbulb_one.__my_list)

print(lightbulb_one.state)
lightbulb_one.turn_on()
print(lightbulb_one.state)
lightbulb_one.turn_off()
print(lightbulb_one.state)


class Computer:

    def __init__(self):
        self.monitor = 'hd'
        self.os = 'Linux'
    def turn_on(self):

        return True

class Dell(Computer):
    def turn_on(self):
        return False

d1 = Computer()
d2 = Dell()
d1.turn_on()
d1 = d2

# print(hash(d1))
# print(hash(d2))
print(d1.turn_on())
print(d2.turn_on())


# models a triangle

class Triangle:

    def calculate_area(self,r):
        self.r = r
        return(3.16*(self.r**2))

if __name__ == '__main__':
    pass

calculate_area_triangle = Triangle(5)
print(calculate_area_triangle.r)
print(calculate_area_triangle.calculate_area(10))
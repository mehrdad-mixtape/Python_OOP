### OOP: Object Oriented Programming

## overloading: You might have wondered how the same built-in operator or
# function shows different behavior for objects of different classes. 
# This is called operator overloading or function overloading respectively.

## overriding: The overriding method allows a child class to provide a specific
# implementation of a method that is already provided by one of its parent classes.

class Car:
    """document of Car"""

    number_of_cars = 0 # class attribute

    # special method: constructor of class, help you to assign attributes to object of class.
    def __init__(self, brand, hp, speed, car_id, price=None):
        print('__init__ was called')
        self.car_brand = brand # instance attribute
        self._horse_power = hp
        self.top_speed = speed
        self._price = price
        self._id = car_id
        Car.number_of_cars += 1

    # special method: description of class.
    # to obtain the user-friendly string representation of the object which can be read by a normal user rather than the programmer.
    # moreover, __str__() is the method that is used by Python when you call print() on your object.
    def __str__(self): # overload str(), It is necessary that __str__() returns a str object, and we get a TypeError if the return type is non-string.
        print('__str__ was called')
        return f"""Car info:
        Brand: {self.car_brand}
        HP: {self.horse_power}
        Top Speed: {self.speed}
        Price: {self.price}"""

    # special method: representation of class.
    # When a class doesn’t implement the __str__ method and you pass an instance of that class to the str(), Python returns the result of the __repr__ method.
    # to obtain the parsable string representation of an object
    def __repr__(self): # overload repr()
        # that means that Python should be able to recreate the object from the representation when repr is used in conjunction with functions like eval().
        print('__repr__ was called')
        return f"Car({self.car_brand}, {self.horse_power}, {self.speed}, {self.price})"

    # special method: destructor of class, helps you delete the object reference.
    def __del__(self):
        print('__del__ was called')
        self = None
        Car.number_of_cars -= 1

    # Properties are class attributes that manage instance attributes.
    # property():
    def _get_speed(self):
        print('_get_speed was called\n')
        return self.top_speed
    def _set_speed(self, value):
        print('_set_speed was called\n')
        if value <= 0:
            raise ValueError('speed of car must be positive')
        self.top_speed = value
    def _del_speed(self):
        print('_del_speed was called\n')
        del self.top_speed
    speed = property(fget=_get_speed, fset=_set_speed, fdel=_del_speed, doc='speed of car') # I should use speed insted of top_speed

    # @property
    @property
    def horse_power(self):
        print('horse_power.getter was called\n')
        return self._horse_power
    # @horse_power.getter
    # def horse_power(self):
    #     print('horse_power.getter was called\n')
    #     return self._horse_power
    @horse_power.setter    
    def horse_power(self, value):
        print('horse_power.setter was called\n')
        if value <= 0:
            raise ValueError('horse power of car must be positive')
        self._horse_power = value
    @horse_power.deleter
    def horse_power(self):
        print('horse_power.deleter was called\n')
        del self._horse_power

    @property # read-only attribute!
    def price(self):
        return self._price
    @price.setter
    def price(self, value):
        raise AttributeError('price is read-only')
    
    @property # write-only attribute!
    def car_id(self):
        raise AttributeError('car_id is write-only')
    @car_id.setter
    def car_id(self, value):
        self._id = value
    def movement(self, meter: int) -> str:
        import os, time
        s = " "
        for m in range(meter):
            time.sleep(0.05) # this function 0.05s get break for print.
            if m % 2 == 0:
                s += " "
                os.system('clear')
                print(s + "        /'''''\      ")
                print(s + " |''''''  -   /''''o ")
                print(s + " =.-(O)--------(O)-.\_")
            else:
                s += " "
                os.system('clear')
                print(s + "        /'''''\      ")
                print(s + " |''''''  -   /''''o ")
                print(s + " =.-(#)--------(#).\_")
        print("have nice time!!!")
    # special method: overload dir()
    def __dir__(self):
        return ['move', 'speed', 'horse_power', 'price', 'car_id']

    # special method: you can check the equality of 2 objects of this class, shortcut ==
    def __eq__(self, other):
        return self.car_brand == other.car_brand and \
            self.horse_power == other.horse_power and \
                self.top_speed == other.top_speed and \
                    self.price == other.top_speed
    
    # special method: you can check the being greater of 2 objects of this class, shortcut >
    def __gt__(self, other):
        return self.car_brand > other.car_brand and \
            self.horse_power > other.horse_power and \
                self.top_speed > other.top_speed and \
                    self.price > other.top_speed

    # special method: you can check the being less of 2 objects of this class, shortcut <
    def __lt__(self, other):
        return self.car_brand < other.car_brand and \
            self.horse_power < other.horse_power and \
                self.top_speed < other.top_speed and \
                    self.price < other.top_speed

    # special method: you can check the inequality of 2 objects of this class, shortcut !=
    def __ne__(self, other):
        return self.car_brand != other.car_brand and \
            self.horse_power != other.horse_power and \
                self.top_speed != other.top_speed and \
                    self.price != other.top_speed

    def __len__(self): # overload len(), It is necessary that __len__() returns a integer object, and we get a TypeError if the return type is non-integer.
        return len()

    def __abs__(self): pass # overload abs()
    def __hash__(self): pass # 

    def __next__(self): pass # overload next()
    def __iter__(self): pass # overload iter()
    def __enter__(self): pass # you can use 'with' keyword for context management
    def __exit__(self): pass # you can use 'with' keyword for context management
    # def __new__(self): pass # meta programing ...
    # more details: https://realpython.com/operator-function-overloading/

# other type manage property
class Coordinate:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        try:
            instance.__dict__[self._name] = float(value)
            print("Validated!")
        except ValueError:
            raise ValueError(f'"{self._name}" must be a number') from None
class Point:
    x = Coordinate()
    y = Coordinate()

    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(12, 5)
print(point.x, point.y)

point.x = 42
print(point.x, '\n')

point.y = 100.0
print(point.y, '\n')

try:
    point.x = "one"
    point.y = "1o"
except ValueError as VE: print(VE)

# cache property:
from time import sleep
class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._diameter = None

    @property
    def diameter(self):
        if self._diameter is None:
            sleep(0.5)  # Simulate a costly computation
            self._diameter = self.radius * 2
        return self._diameter

circle = Circle(42.0)
print(circle.diameter, '\n')  # With delay

print(circle.diameter, '\n')  # Without delay

circle.radius = 100
print(circle.diameter, '\n')  # Wrong diameter

class TreeNode:
    def __init__(self, data):
        self._data = data
        self._children = []

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, value):
        if isinstance(value, list):
            self._children = value
        else:
            del self.children
            self._children.append(value)

    @children.deleter
    def children(self):
        self._children.clear()

    def __repr__(self):
        return f'{self.__class__.__name__}("{self._data}")'
    
root = TreeNode("root")
child1 = TreeNode("child 1")
child2 = TreeNode("child 2")

root.children = [child1, child2]

print(root.children, '\n')

del root.children
print(root.children, '\n')

# overriding property
class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value
class Employee(Person):
    @property
    def name(self):
        return super().name.upper()

person = Person("John")
print(person.name, '\n')

person.name = "John Doe"
print(person.name, '\n')

employee = Employee("John")
print(employee.name, '\n')

def main():
    my_car = Car('Dodge', 840, 360, '43hgt-1',price=31_000)
    print('my_car was initialized\n')
    print(my_car.car_brand, '\n')
    print(my_car, '\n')
    print(my_car.__doc__, '\n')
    print(my_car.__dict__, '\n')

    my_car.car_brand = 'Ford' # set value for attribute with property

    my_car = Car('Ford', 700, 330, 'hs943-1', price=40000)
    try:
        print(my_car.horse_power)
        my_car.horse_power = -700
    except ValueError as VE:
        print(VE)
        del my_car.horse_power # call horse_power.deleter

    print(my_car.__init__('Ferrari', 1100, 380, '904hf-w',price=60000), '\n') # create object but return None
    print(my_car.__class__('Ferrari', 1100, 380, '904hf-w', price=60000), '\n') # create object and return it
    print(my_car.__dict__, '\n')
    try:
        my_car.price = 70000
    except AttributeError as AE:
        print(AE, '\n')
    try:
        print(my_car.car_id, '\n')
    except AttributeError as AE:
        print(AE, '\n')

    print(dir(my_car), '\n')
    
    del my_car # call the __del__

    print('my_car was deleted\n')
    try:
        print(my_car.car_brand, '\n')
    except UnboundLocalError as ULE:
        print(ULE)

if __name__ == '__main__':
    main()

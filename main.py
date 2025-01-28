class Natural:
    @classmethod
    def __check_value(self, value):
        if type(value) not in (int, float):
            raise ValueError("Value type must be int or float")
        elif value < 0:
            raise ValueError("Value must be greater than zero")
        else:
            return value
    
    def __set_name__(self, owner, name):
        self.name = "__" + name
        
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        return setattr(instance, self.name, self.__check_value(value))

class Point:
    x = Natural()
    y = Natural()
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
point_one = Point(4, 3)
print(point_one.x)
point_one.x = 1
class Natural:
    def __set_name__(self, owner, name):
        self.name = "__" + name
        
    def __get__(self, instance, owner):
        return getattr(instance, self.name)
    
    def __set__(self, instance, value):
        if value > 0:
            return setattr(instance, self.name, value)
        else:
            raise ValueError("X must be greater than zero")

class Point:
    x = Natural()
    y = Natural()
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
point_one = Point(4, 3)
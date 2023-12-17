import math 

class MyMath:
    pi = math.pi

    @classmethod
    def circle_len(cls, radius: float) -> float:
        return 2 * cls.pi * radius

    @classmethod
    def circle_area(cls, radius: float) -> float:
        return cls.pi * radius * radius

    @classmethod
    def cube_surface_area(cls, side_len: float) -> float:
        return 6 * side_len * side_len

    @classmethod
    def cube_volume(cls, side_len: float) -> float:
        return side_len ** 3

    @classmethod
    def sphere_surface_area(cls, radius: float) -> float:
        return 4 * cls.pi * radius * radius

    @classmethod
    def sphere_volume(cls, radius: float) -> float:
        return 4 / 3 * cls.pi * radius ** 3
    
    @classmethod
    def rectangle_area(cls, side_a: float, side_b: float) -> float:
        return side_a * side_b
    

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_area(radius=6)
res_3 = MyMath.rectangle_area(side_a=2, side_b=2)
print(res_1)
print(res_2)
print(res_3)
class Element:
    def __str__(self):
        return type(self).__name__

    def __add__(self, other):
        self_type = type(self)
        other_type = type(other)
        if self_type == other_type:
            return self
        if (self_type, other_type) in elements:
            return elements[(self_type, other_type)]()
        if (other_type, self_type) in elements:
            return elements[(other_type, self_type)]()
        return None


class Water(Element):
    pass


class Air(Element):
    pass


class Fire(Element):
    pass


class Earth(Element):
    pass


class Storm(Element):
    pass


class Steam(Element):
    pass


class Dirt(Element):
    pass


class Lightening(Element):
    pass


class Dust(Element):
    pass


class Lava(Element):
    pass


class Hydrolightening(Element):
    pass


elements = {
    (Water, Air): Storm,
    (Water, Fire): Steam,
    (Water, Earth): Dirt,
    (Air, Fire): Lightening,
    (Air, Earth): Dust,
    (Fire, Earth): Lava,
    (Lightening, Water): Hydrolightening
}

air = Air()
fire = Fire()
water = Water()

result = (air + fire) + water
print(result)
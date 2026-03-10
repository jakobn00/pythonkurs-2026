############# Labb 5 #######################
# %% 4.1.1
import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def spherical(self):
        r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        theta = math.atan2(self.z, math.sqrt(self.x**2 + self.y**2))
        phi = math.atan2(self.y, self.x)
        return (r, theta, phi)

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    # For testing
    def print_spherical_degrees(self):
        r, theta, phi = self.spherical()
        factor = 360 / (2 * math.pi)
        theta *= factor
        phi *= factor
        print(f"{theta=:.2f}, {phi=:.2f}")

a = Point(1 / math.sqrt(2), 1 / math.sqrt(2), -1)
a.print_spherical_degrees()
print(a)
print(a.distance())
# %% 4.2.2
# TODO: redovisa denna

class Klass:
    def __init__(self, d):
        for k, v in d.items():
            setattr(self, k, v)
    
    def remove_attr(self, attr):
        delattr(self, attr)
    
    def add_attr(self, attr, value):
        if not hasattr(self, attr):
            setattr(self, attr, value)
    
    def update_attr(self, attr, value):
        if hasattr(self, attr):
            setattr(self, attr, value)

    def __str__(self):
        d = self.__dict__
        keys = (" " * 5).join(str(k) for k in d.keys())
        base = " " * 10
        keys = [str(k) + base[len(str(k)):] for k in d.keys()]
        key_row = " | ".join(keys)
        values = [str(k) + base[len(str(k)):] for k in d.values()]
        value_row = " | ".join(values)
        dashes = "-" * (13 * len(d))
        out = f"""
        {dashes}
        | {key_row} |
        {dashes}
        | {value_row} |
        {dashes}
        """
        return out


d = {
    "fruit": 1,
    "book": 2,
    "word": "mattress",
}
c = Klass(d)
print(c)

c.remove_attr("book")
print(c)

c.add_attr("sponge", "yellow")
print(c)

c.update_attr("fruit", "banana")
print(c)

# %% 4.3.3


class Vektor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def R(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    @classmethod
    def new(cls, x, y, z):
        return cls(x, y, z)


v = Vektor(1, 1, 1)
print(v)
print(v.R())
u = Vektor.new(2, 3, 4)
print(u)

# %% 4.4.1


class Person:
    def __init__(self, namn, personnummer):
        self.namn = namn
        self.personnummer = personnummer

    def __str__(self):
        attrs = ", ".join(f"{k}={v}" for k, v in self.__dict__.items())
        return attrs


class Bilist(Person):
    def __init__(self, namn, personnummer, körkortsnivå):
        super().__init__(namn, personnummer)
        self.körkortsnivå = körkortsnivå


def har_körkort(obj):
    return isinstance(obj, Bilist)


p = Person("Jakob", "2000")
b = Bilist("Jakob", "2000", "B")

print(p)
print(b)
print(har_körkort(p))
print(har_körkort(b))

# %% 4.5.2

class Vektor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vektor(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )
    
    def __sub__(self, other):
        return Vektor(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __matmul__(self, other):
        return Vektor(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
    

u = Vektor(1, 2, 3)
v = Vektor(4, 5, 6)

w = u + v
print(w)

w = u - v
print(w)

w = u * v
print(w)

w = u @ v
print(w)
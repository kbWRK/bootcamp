class Vector:
    def __init__(self,x , y):
        self.x = x
        self.y = y

    def __str__(self):
         return f"vector ({self.x}, {self.y})"

    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        if isinstance(other,Vector):
            return Vector(self.x * other.x, self.y * other.y)
        else:
            return Vector(self.x * other, self.y * other)

   def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def test_vector_init():
    v1 = Vector(1, 2)
    assert v1.x == 1
    assert v1.y == 2
def test_vector_str():
    v1 = Vector(1, 2)
    assert str(v1) == "Vector(1, 2)"
def test_vector_add():
    v1 = Vector(1, 2)

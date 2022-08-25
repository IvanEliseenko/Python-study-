
class Road:
    def __init__(self, length, wide):
        self.length = length
        self.wide = wide

    def AsphMass(self, mass=25, thickness=5):
        return self.length * self.wide * mass * thickness / 1000


road_1 = Road(int(input("Input length: ")), int(input("Input wide: ")))
print(road_1.AsphMass())
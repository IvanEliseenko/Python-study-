from random import choice


class Car:
    direction = ["north", "south", "east", "west"]

    def __init__(self, speed, color, name, police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = police

    def go(self):
        return f"{self.name} is moving."

    def stop(self):
        return f"{self.name} is stopped"

    def turn(self):
        return f"{self.name} is turn {choice(self.direction)}"

    def show_speed(self):
        return f"{self.name} speed is {self.speed}"


class TownCar(Car):
    def show_speed(self):
        return f"Speeding! Speed is {self.speed}" if self.speed > 60 else f"{self.speed}"


class SportCar(Car):
    def show_speed(self):
        return f"{self.speed}"


class WorkCar(Car):
    def show_speed(self):
        return f"Speeding! Speed is {self.speed}" if self.speed > 40 else f"{self.speed}"


class PoliceCar(Car):
    def __init__(self, speed, color, name, police=False):
        super().__init__(speed, color, name, police=True)


town_car = TownCar(45, "Blue", "Town Car")
sport_car = SportCar(80, "Red", "Sport Car")
work_car = WorkCar(55, "Yellow", "Bus")
police_car = PoliceCar(80, "Blue", "Polizia")

car_list = [town_car, sport_car, work_car, police_car]

for i in car_list:
    print(i.go())
    print(i.show_speed())
    print(i.stop())
    print(i.turn())
    print(i.show_speed())

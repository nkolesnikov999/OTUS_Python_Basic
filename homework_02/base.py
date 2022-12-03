from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):

    started = False

    def __init__(self, weight=1000, fuel=0, fuel_consumption=20):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance):
        max_distance = self.fuel // self.fuel_consumption
        if distance <= max_distance:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel



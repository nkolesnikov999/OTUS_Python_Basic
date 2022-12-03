"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int

    def __init__(self, weight=1000, fuel=0, fuel_consumption=20, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, cargo):
        if self.max_cargo >= self.cargo + cargo:
            self.cargo += cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        cargo = self.cargo
        self.cargo = 0

        return cargo

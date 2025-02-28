from abc import ABC, abstractmethod

import Factory.product as product

class VehicleFactory(ABC):
    @abstractmethod
    def create(self, vehicle_type):
        pass
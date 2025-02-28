from abc import ABC, abstractmethod

# Clase abstracta Factory
import product as product

class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self, vehicle_type):
        pass
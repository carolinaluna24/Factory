from abc import ABC, abstractmethod

class  Vehicle(ABC):
    @abstractmethod
    def envios(self):
        pass

class Car(Vehicle):
    def __init__(self, modelo):
        self.modelo = modelo
        
    def envios(self):
        return f"el carro es modelo {self.modelo}"
   
class Moto(Vehicle):
    def __init__(self, modelo):
        self.modelo = modelo
        
    def envios(self):
        return f"el moto es modelo {self.modelo}"

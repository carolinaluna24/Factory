from abc import ABC, abstractmethod

#Clase base para toos los vehículos
class  Vehicle(ABC):
    @abstractmethod
    def envios(self):
        pass

#clase carro
class Car(Vehicle):
    def __init__(self, modelo, color, year):
        self.modelo = modelo
        self.color = color
        self.year = year
        
    def envios(self):
        return f"El carro es modelo {self.modelo}, color {self.color}, año {self.year}"

#clase moto
class Moto(Vehicle):
    def __init__(self, modelo, color, year):
        self.modelo = modelo
        self.color = color
        self.year = year
        
    def envios(self):
        return f"Moto: modelo {self.modelo}, color {self.color}, año {self.year}"

#clase camión
class Truck(Vehicle):
    def __init__(self, modelo, color, year):
        self.modelo = modelo
        self.color = color
        self.year= year

    def envios(self):
        return f"Camión: modelo {self.modelo}, color {self.color}, año {self.year}"
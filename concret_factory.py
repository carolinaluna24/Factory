from product import Car, Moto, Truck
from creator import VehicleFactory

#Manipulador de factories

class CarFactory(VehicleFactory):
    #crea un objeto de la clase carro
    def create_vehicle(self, vehicle_type, color, year):
        #sobreescribe el método de la clase abstracta
          return Car(vehicle_type)
          #retorna un objeto de la clase

class MotoFactory(VehicleFactory):
    #crea un objeto de la clase moto
    def create_vehicle(self, vehicle_type, color, year):
          return Moto(vehicle_type)

class TruckFactory(VehicleFactory):
    #crea un objeto de la clase camión
    def create_vehicle(self, vehicle_type,color, year):
         return Truck(vehicle_type, color, year)

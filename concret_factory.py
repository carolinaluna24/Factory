from Factory.product import Car, Moto
from Factory.creator import VehicleFactory

#Manipulador de factories

class CarFactory(VehicleFactory):
    #crea un objeto de la clase
    def create_vehicle(self, vehicle_type):
        #sobreescribe el método de la clase abstracta
          return Car(vehicle_type)
          #retorna un objeto de la clase

class MotoFactory(VehicleFactory):
    def create_vehicle(self, vehicle_type):
          return Moto(vehicle_type)
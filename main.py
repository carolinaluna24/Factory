# archivo para cosumir todo, se consumen las fábricas y se envia los datos a las clases

from concret_factory import CarFactory, MotoFactory, TruckFactory
#traemos la clase que creamos Car y Moto

from client_test import client_vehicle
#traemos la funcion que llama a la clase

#Entrada principal

if __name__ == "__main__":
  #usamos if__name__ para que no se ejecute el codigo si se importa
  #creamos un objeto de la clase , una fábrica
  car_factory = CarFactory()
  moto_factory = MotoFactory()
  truck_factory = TruckFactory()

  #pasamos los parametros necesarios
  #usamos las fábricas a través de la función client
  client_vehicle(car_factory, "Ferrari", "Rojo", "2020")
  client_vehicle(moto_factory, "Honda", "Azul", "2025")
  client_vehicle(truck_factory, "Fotón", "Blanco", "2022")
  
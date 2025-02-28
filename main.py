# archivo para cosumir todo

from concret_factory import CarFactory, MotoFactory
#traemos la clase que creamos Car y Moto

from client_test import client_vehicle
#traemos la funcion que llama a la clase

#Entrada principal

if __name__ == "__main__":
  #usamos if__name__ para que no se ejecute el codigo si se importa
  #creamos un objeto de la clase , una fábrica
  car_factory = CarFactory()
  moto_factory = MotoFactory()

  #pasamos los parametros necesarios
  #usamos las fábricas a través de la función client
  client_vehicle(car_factory, "Ferrari")
  client_vehicle(moto_factory, "Honda")
  
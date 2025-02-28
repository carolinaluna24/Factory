# archivo para cosumir todo

from concret_factory import CarFactory, MotoFactory
#traemos la clase que creamos Car y Moto

from client_test import client_vehicle
#traemos la funcion que llama a la clase

if __name__ == "__main__":
  #usamos if__name__ para que no se ejecute el codigo si se importa
  #creamos un objeto de la clase
  car_factory = CarFactory()
  moto_factory = MotoFactory()

  #pasamos los parametros necesarios
  client_vehicle(car_factory, "Ferrari")
  client_vehicle(moto_factory, "Honda")
  
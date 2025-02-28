def client_vehicle(factory, vehicle_tipe):
  vehicle = factory.create(vehicle_tipe)
  print(vehicle.envios())
# Función cliente que consume una fábrica
def client_vehicle(factory, vehicle_tipe):
  vehicle = factory.create_vehicle(vehicle_tipe)
  print(vehicle.envios())
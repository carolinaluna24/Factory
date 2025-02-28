# Función cliente que consume una fábrica
def client_vehicle(factory, vehicle_tipe, color, year):
  vehicle = factory.create_vehicle(vehicle_tipe, color, year)
  print(vehicle.envios())
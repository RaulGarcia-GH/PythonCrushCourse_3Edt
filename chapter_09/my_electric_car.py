# from car_class import ElectricCar
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())
# my_leaf.battery.describe_battery()
# my_leaf.battery.get_range()
# my_leaf.battery.upgrade_battery()
# my_leaf.battery.get_range()

# from car_class import Car, ElectricCar
# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# import car_class
# my_mustang = car_class.Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = car_class.ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# from car_class import Car
# from car_electric_class import ElectricCar
# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# from car_electric_class import ElectricCar as EC
# my_leaf = EC('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

import car_electric_class as ec
my_leaf = ec.ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
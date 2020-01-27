# from car_store import Car,ElectricCar 从一个模块中导入多个类

import car_store #导入整个块

my_beetle = car_store.Car('volkswagen','beetle',2016)
print(my_beetle.get_descriptive_name())
my_tesla = car_store.ElectricCar('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())

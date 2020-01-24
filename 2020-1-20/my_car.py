from electricCar import Car

my_car = Car('tesla','model 3','2019')
print(my_car.get_descriptive_name())

my_car.read_odometer()
my_car.increasement_odometer(10000)
my_car.read_odometer()


class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    
    def read_odometer(self):
        print ("This car has "+str(self.odometer_reading)+" miles on it")
    
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increasement_odometer(self,miles):
        self.odometer_reading += miles

my_new_car = Car('audio','a4','2016')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 100000000 #直接修改属性 
my_new_car.read_odometer()

my_new_car.update_odometer(22222)
my_new_car.read_odometer()

my_new_car.increasement_odometer(789)
my_new_car.read_odometer()

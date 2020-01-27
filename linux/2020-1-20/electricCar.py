class Car():
    def __init__(self,make,model,year):             #__init__是一个特殊的方法每当你根据car创建新实例时python都会自动运行它
        self.make = make                            #获取存储在形参变量中的值　像这样可以通过实例来访问的对象我们称之为属性
        self.model = model              
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):                 #定义在类中的方法
        long_name = str(self.year)+' '+self.make+' '+self.model
        return long_name.title()
    
    def read_odometer(self):
        print ("This car has "+str(self.odometer_reading)+" miles on it")
    
    def update_odometer(self,mileage):               #通过方法修改属性的值
        if mileage>=self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increasement_odometer(self,miles):           #通过方法对属性的值进行递增
        self.odometer_reading += miles

#my_new_car = Car('audio','a4','2016')               #my_new_car就是实例
#print(my_new_car.get_descriptive_name())

class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size=battery_size
    
    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kWh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range  = 270
        message = "This car can go approximately "+str(range)
        message += " miles on a full charge"
        print(message)

class EletricCar(Car):                              #继承了父类Car定义子类时必须在括号内指明父类的名称
    def __init__(self,make,model,year):             #接受创建car实例所需的信息
        super().__init__(make,model,year)           #super是一个特殊函数，将父类和子类联系起来　
        self.battery=Battery()                      #将battery实例用作属性

my_tesla = EletricCar('tesla','model_s',2016)       #这行代码调用EletricalCar中的__init__()后者让python调用父类Car中__init__()

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

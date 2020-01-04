class Dog():
    def __init__(self,name,age):   #__init__是一个方法
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+" is now sitting.")

    def roll_over(self):
        print(self.name.title()+" rolled over!")
my_dog = Dog('willie',6)
your_dog = Dog('lucy',3)

print("My dog's name is "+ my_dog.name.title()+".")
print("My dog's age is "+ str(my_dog.age)+"years old")
my_dog.sit()
my_dog.roll_over()

print("Your dog's name is "+your_dog.name.title()+".")
print("Your dog's age is "+str(your_dog.age)+" years old" )
your_dog.sit()
your_dog.roll_over()


def printline():
    print("======================================================================")

def greeter_user():
    """Dispaly a simple greeting"""
    print("Hello!")
greeter_user()
printline()

def greeter_user1(username):
    print("Hello "+username.title()+" !")

greeter_user1("xiaomi")
def make_car(manufacture,model,**car_info):
    info = {}
    info['manufacture']=manufacture
    info['model']=model
    for key,value in car_info.items():
        info[key]=value
    return info 
car = make_car('subaru','outback',color='blue',tow_package=True)
print (car)

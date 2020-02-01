import json

numbers = [2,3,4,7,11,12,13]

filename = 'number.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

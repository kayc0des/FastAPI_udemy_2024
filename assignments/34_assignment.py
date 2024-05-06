''' Python Dictionaries '''

my_vehicle = {
    'model': 'Ford',
    'make': 'Explorer',
    'year': 2018,
    'mileage': 40000    
}

# create a loop to print all keys and values
for key, value in my_vehicle.items():
    print(f'{key} has a value of {value}')

# create vehicle2 a copy of my_vehicle
vehicle2 = my_vehicle.copy()

# add a new key to vehicle2
vehicle2['number_of_tires'] = 4
print(vehicle2)

# Delete the mileage key and value
vehicle2.pop('mileage')
print(vehicle2)

# print all the keys in vehicle2
for key in vehicle2:
    print(key)
import InsectClass as i

mosquito = i.Insect(2,4,'mosquito')
housefly = i.Insect(2,4,'housefly')

#Set/mutator method
mosquito.calc_flight()
housefly.calc_flight()

#Get/accessor method
print(f'The {mosquito.get_name()} can travel up to {mosquito.get_miles()} miles')
print(f'The {housefly.get_name()} can travel up to {housefly.get_miles()} miles')
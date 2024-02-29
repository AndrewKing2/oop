import CellPhoneClass as c


manufacturer = input('Who is the manufacturer? ')
model = input('What is the model number? ')
price = int(input('What is the price? '))


iphone15 = c.CellPhone(manufacturer, model, price)

iphone15.set_retail_price(int('999'))

print(f'The {iphone15.get_manufact()} {iphone15.get_model()} costs ${iphone15.get_retail_price():.2f}')
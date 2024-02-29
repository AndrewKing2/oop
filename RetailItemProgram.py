import RetailItemClass as r

item1 = r.RetailItem('Jacket',12,59.95)
item2 = r.RetailItem('Designer Jeans',40,34.95)
item3 = r.RetailItem('Shirt',20,24.95)

print(f'We currently have {item1.get_unit()} {item1.get_desc()}s that can be sold for ${item1.get_price():.2f} each')
print(f'We currently have {item2.get_unit()} pairs of {item2.get_desc()} that can be sold for ${item2.get_price():.2f} each')
print(f'We currently have {item3.get_unit()} {item3.get_desc()}s that can be sold for ${item3.get_price():.2f} each')
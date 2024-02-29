class RetailItem:

    def __init__(self,desc,unit,price):
        self.__desc = desc
        self.__unit = unit
        self.__price = price

    def get_desc(self):
        return self.__desc
    
    def get_unit(self):
        return self.__unit
    
    def get_price(self):
        return self.__price
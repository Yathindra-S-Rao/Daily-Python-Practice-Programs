class Television:
    
    def __init__(self, brand, model, display_type, size, price):
        self.brand = brand
        self.__model = model
        self.display_type = display_type
        self.screen_size = size
        self.__price = price
        
    def get_model(self):
        return self.__model
        
    def get_price(self):
        return f"{self.__price}"
    
    def get_tv_details(self):
        return f'''{self.brand.upper()} - {self.get_model()} {self.screen_size}" {self.display_type} Disply '''
        
    def set_model(self, model):
        try:
            self.__model = model
            return "Model name updated successfully"
        except:
            print('Unexpected error occured while updating Model name')

    def set_price(self, price):
        try:
            self.__price = price
            return "Price updated successfully"
        except:
            print('Unexpected error occured while updating Price')

t1 = Television('Onida', 'Xperia', 'OLED', 42, 34999.00)
print(t1.get_tv_details())
print(t1.set_model('Cardio'))
print(t1.get_tv_details())
print(t1.set_price(33999.32))
print(t1.get_price())




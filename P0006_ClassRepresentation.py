class Fruit:
    
    def __init__(self, fruit, price):
        self.fruit = fruit
        self.price = price
    
    def __str__(self):
        return f"{self.fruit} - Rs.{self.price}"
        
f1 = Fruit("Banana", 40.50)
print(f1)
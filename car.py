class Car:
    def __init__(self,wheels,fuel,brand,x):
        self.wheels=wheels
        self.fuel=fuel
        self.brand=brand
        self.x=x
    def drive(self):
        self.fuel-=1
        self.x+=10
    def __str__(self):
        return f"{self.wheels} {self.brand} {self.fuel}"
    def car_accident(self,other):
        if self.x==other.x:
            return True
        else:
            return False
        
    
    
carts=Car(4,50,"lancrozen",0)
wheelsgyat=Car(3,70,"gyatcar",50)
print(carts,wheelsgyat)
carts.car_accident(wheelsgyat)
print(carts.car_accident(wheelsgyat))
while carts.car_accident(wheelsgyat) == False:
   carts.drive()
   print(carts.x,wheelsgyat.x)

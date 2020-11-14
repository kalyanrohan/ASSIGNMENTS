class Car:
    def __init__(self,model,speed,tank_capacity,fuel_usage):
        self.model=str(model)
        self.speed=int(speed)
        self.tank_capacity=float(tank_capacity)
        self.fuel_usage=float(fuel_usage)
    

    def max_distance(self):
        result=self.tank_capacity/self.fuel_usage
        return result
    

    def max_duration(self):
        result= self.max_distance()/self.speed
        return result
    

    def is_better_than(self,other_car):
        if self.max_duration()>other_car.max_duration() and self.max_distance()>other_car.max_distance():
            return "yes"
        elif self.max_duration()>other_car.max_duration() or self.max_distance()>other_car.max_distance():
            return "maybe"
        else:
            return "no"
    
    
    def compare_cars(self,other_company):
        x=0
        for car in other_company.cars:
            if self.is_better_than(car)=="yes":
                x+=1
        print_statement=print(f"The car, {self.model} is better than {str(x)} out of {len(other_company.cars)} of all the cars in {other_company.name}")


class Company:
    def __init__(self,name,cars):
        self.name=str(name)
        self.cars=cars

car1 = Car("Model S", 50, 37, 8.5)
car2 = Car("Model 3", 45, 40, 10.2)
car3 = Car("Model X", 55, 46, 7.9)
car4 = Car("Rock", 50, 45, 9.4)

company1 = Company("Tebsla", [car1, car2, car3])

print(car4.is_better_than(car1))
print(car2.is_better_than(car3))
print(car1.is_better_than(car2))

car4.compare_cars(company1)

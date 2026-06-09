cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235}
]

def calculate_mpg(car):     # parameter
# variable that accepts a value inside the function
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['make']} {car['model']}"
    print(f"{name} does {mpg} miles per gallon.")

for car in cars:            
    calculate_mpg(car)      # argument 
    # value you pass in to the function
    
'''
Ford Fiesta does 50.0 miles per gallon.
Ford Focus does 48.57142857142857 miles per gallon.
Mazda MX-5 does 54.44444444444444 miles per gallon.
Mini Cooper does 131.91489361702128 miles per gallon.
'''

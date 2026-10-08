from pizza import Pizza
from decorator import Decorator
from addons import Jalapeno,Onion,Tomato,Cheese,Chicken,Brocolli

pizza1 = Pizza()
print(f" Pizza Desc:{pizza1.get_desc()}, Pirce: {pizza1.get_cost()}")
pizza1 = Jalapeno(pizza1)
pizza1 = Onion(pizza1)
pizza1 = Tomato(pizza1)
print(f" Pizza Desc:{pizza1.get_desc()}, Pirce: {pizza1.get_cost()}")

pizza2 = Pizza()
toppings = (
    Jalapeno,
    Onion,
    Tomato,
    Cheese,
    Chicken,
    Brocolli,
)

for topping in toppings:
    pizza2 = topping(pizza2)
print(f" Pizza Desc:{pizza2.get_desc()}, Pirce: {pizza2.get_cost()}")
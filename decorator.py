from food import Food
from pizza import Pizza

class Decorator(Food):

    def __init__(self,pizza: Pizza):
        self._pizza = pizza

    def get_desc(self):
        return self._pizza.get_desc()

    def get_cost(self):
        return self._pizza.get_cost()

    
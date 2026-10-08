from decorator import Decorator

class Jalapeno(Decorator):

    def get_desc(self):
        return super().get_desc() + " , Jalapeno"

    def get_cost(self):
        return super().get_cost() + 1

class Onion(Decorator):

    def get_desc(self):
        return super().get_desc() + " , Onion"

    def get_cost(self):
        return super().get_cost() + 1

class Tomato(Decorator):

    def get_desc(self):
        return super().get_desc() + " , Tomato"

    def get_cost(self):
        return super().get_cost() + 1


class Brocolli(Decorator):

    def get_desc(self):
        return super().get_desc() + " , Broco"

    def get_cost(self):
        return super().get_cost() + 1


class Chicken(Decorator):

    def get_desc(self):
        return super().get_desc() + " , Chicken"

    def get_cost(self):
        return super().get_cost() + 3


class Cheese(Decorator):

    def get_desc(self):
        return super().get_desc() + " , Extra Cheese"

    def get_cost(self):
        return super().get_cost() + 2
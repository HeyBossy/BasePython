class Ingredient:
    def __init__(self, name_ingr: str, weight: float, cost: float):
        self.name_ingr = name_ingr
        self.weight = weight
        self.cost = cost

    def get_name(self) -> str:
        '''Возвращает название ингредиента.'''
        return self.name_ingr

    def get_weight(self) -> float:
        '''Возвращает вес в граммах.'''
        return self.weight

    def get_cost(self) -> float:
        '''Возвращает стоимость в рублях.'''
        return self.cost


class Pizza:
    def __init__(self, name_pizza):
        self.name_pizza = name_pizza
        self.lst_ingridients = []

    def get_name_pizza(self) -> str:
        '''Возвращает название пиццы.'''
        return self.name_pizza

    def add_ingredient(self, ingridient: Ingredient):
        ''' принимает объект типа Ingredient и добавляет ингредиент в пиццу'''
        self.lst_ingridients.append(ingridient)

    def get_weight_pizza(self) -> float:
        ''' возвращает вес пиццы в килограммах (1кг=1000г)'''
        return (sum(ingridient.get_weight() for ingridient in self.lst_ingridients)) / 1000

    def get_cost_pizza(self) -> float:
        ''' возвращает стоимость пиццы в рублях.'''
        return sum(ingridient.get_cost() for ingridient in self.lst_ingridients)

class Order:
    def __init__(self):
        self.lst_pizzas = []

    def add_pizza(self, pizza: Pizza):
        self.lst_pizzas.append(pizza)

    def get_cost_order(self) -> float:
        '''  возвращает стоимость заказа в рублях.'''
        return sum(pizza.get_cost_pizza() for pizza in self.lst_pizzas)

    def print_receipt(self) -> str:
        for pizza in self.lst_pizzas:
            print(f'{pizza.get_name_pizza()} ({pizza.get_weight_pizza():.3f}кг) - {pizza.get_cost_pizza():.2f}руб \n')


if __name__ == '__main__':
    cream_sauce = Ingredient('Сливочный соус', 50, 50)
    blue_cheese = Ingredient('Сыр блю чиз', 100, 100)
    mozzarella = Ingredient('Моцарелла', 100, 100)
    cheddar = Ingredient('Чеддер', 100, 100)
    parmesan = Ingredient('Пармезан', 100, 100)

    pizza = Pizza('Четыре сыра')
    pizza.add_ingredient(cream_sauce)
    pizza.add_ingredient(blue_cheese)
    pizza.add_ingredient(mozzarella)
    pizza.add_ingredient(cheddar)
    pizza.add_ingredient(parmesan)

    order = Order()
    order.add_pizza(pizza)
    order.add_pizza(pizza)
    order.add_pizza(pizza)

    print(pizza.get_cost_pizza())
    print(pizza.get_weight_pizza())
    print(order.get_cost_order())
    order.print_receipt()
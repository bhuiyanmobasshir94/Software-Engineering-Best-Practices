## Creational Pattern

### Factory Design Pattern

class Burger:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def print(self):
        print(self.ingredients)

class BurgerFactory:
    def createCheeseBurger(self):
        ingredients = ["Cheese", "Bun", "Beef-petty"]
        return Burger(ingredients)
    
    def createDeluxeCheeseBurger(self):
        ingredients = ["Cheese", "Bun", "Beef-petty", "Lettuce", "Tomatoe"]
        return Burger(ingredients)

    def createVeganBurger(self):
        ingredients = ["Bun", "Vegan-petty", "Lettuce", "Tomatoe"]
        return Burger(ingredients)

burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurger().print()
burgerFactory.createDeluxeCheeseBurger().print()
burgerFactory.createVeganBurger().print()

### Builder Pattern

class Burger:
    def __init__(self) -> None:
        self.buns = None
        self.patty = None
        self.cheese = None

    def setBuns(self, bunStyle):
        self.buns = bunStyle

    def setPatty(self, pattyStyle):
        self.patty = pattyStyle

    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle

class BurgerBuilder:
    def __init__(self) -> None:
        self.burger = Burger()

    def addBuns(self, bunStyle):
        self.burger.setBuns(bunStyle)
        return self

    def addPatty(self, pattyStyle):
        self.burger.setPatty(pattyStyle)
        return self

    def addCheese(self, cheeseStyle):
        self.burger.setCheese(cheeseStyle)
        return self

    def build(self):
        return self.burger

burger = BurgerBuilder().addBuns("Sesame").addPatty("Fiash-patty").addCheese("Swise-cheese").build()

### Singletone Pattern


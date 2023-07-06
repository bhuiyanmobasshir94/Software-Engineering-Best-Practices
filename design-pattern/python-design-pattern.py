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

class ApplicationState:
    instance = None

    def __init__(self) -> None:
        self.isLoggedIn = False

    @staticmethod
    def getAppState():
        if not ApplicationState.instance:
            ApplicationState.instance = ApplicationState()
        return ApplicationState.instance

appState1 = ApplicationState.getAppState()
print(appState1.isLoggedIn)

appState2 = ApplicationState.getAppState()
appState1.isLoggedIn = True

print(appState1.isLoggedIn)
print(appState2.isLoggedIn)

## Behavioral Pattern

### Observer i.e PubSub

class youtubeChannel:
    def __init__(self, name) -> None:
        self.name = name
        self.subscribers = []
    
    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self, event):
        for sub in self.subscribers:
            sub.sendNotification(self.name, event)
        
from abc import ABC, abstractmethod

class YoutubeSubscriber(ABC):
    @abstractmethod
    def sendNotification(self, channel, event):
        pass

class YoutubeUser(YoutubeSubscriber):
    def __init__(self, name) -> None:
        self.name = name

    def sendNotification(self, channel, event):
        print("Print info")

channel = youtubeChannel("Neetcode")
channel.subscribe(YoutubeUser("sub1"))
channel.subscribe(YoutubeUser("sub2"))
channel.subscribe(YoutubeUser("sub3"))
channel.notify("A new video realeased.")

### Iterator

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.cur = None

    # Define Iterator
    def __iter___(self):
        self.cur = self.head
        return self

    # Iterate
    def __next__(self):
        if self.cur:
            val = self.cur.val
            self.cur = self.cur.next
            return val
        else:
            raise StopIteration

# initialize LinkedList

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
myList = LinkedList(head)

# iterate over the linked list

for n in myList:
    print(n)

### Strategy Pattern



"""
Creational Pattern - Builder 建造者模式
將一個複雜物件的建構與他的表示分離，使得同樣的建構過程可以建立不同的表示。
"""


class Burger:
    def __init__(self):
        self.bun = None
        self.patty = None
        self.cheese = None

    def setBuns(self, bunStyle):
        self.bun = bunStyle

    def setPatty(self, pattyStyle):
        self.patty = pattyStyle

    def setCheese(self, cheeseStyle):
        self.cheese = cheeseStyle


class BurgerBuilder:
    def __init__(self):
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


burger = BurgerBuilder()\
    .addBuns("sesame")\
    .addPatty("fish-patty")\
    .addCheese("swiss cheese")\
    .build()

print(burger.bun)
print(burger.cheese)
print(burger.patty)

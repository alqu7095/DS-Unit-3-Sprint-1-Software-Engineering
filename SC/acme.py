import random

class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                identifier = random.randint(100000000, 9999999)) :
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        if (self.price/self.weight) < 0.5:
            return "not so stealable..."
        elif (self.price/self.weight) <1.5:
            return "kinda stealable"
        else:
            return "very stealable"

    def explode(self):
        if self.weight * self.flammability < 10:
            return "...fizzle"
        elif self.weight * self.flammability < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"
        
class BoxingGlove(Product):
    def __init__(self, name, price=10, weight=10, flammability=0.5, identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier
    
    def explode(self):
        return '...its a glove.'

    def punch(self):
        if self.weight<5:
            return 'that tickles'
        if self.weight>=5 and self.weight<15:
            return 'hey that hurt!'
        else:
            return 'OUCH!'

    

    


import json


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price}"

    @classmethod
    def createFromDict(cls, source: dict):
        return cls(source['name'], source['price'])


p = Product("PowerBeats Pro", 21500)
jsonstr = json.dumps(p.__dict__)
print('JSON ->', jsonstr)
pd = json.loads(jsonstr)
p = Product.createFromDict(pd)
print(p)

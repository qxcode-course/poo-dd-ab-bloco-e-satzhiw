from abc import ABC, abstractmethod
from enum import Enum

class Valuable:
    def getLabel(self) -> str:
        pass
    def getValue(self) -> float:
        pass
    def getVolume(self) -> int:
        pass

class Coin(Valuable, Enum):
    M10 = (0.10, 1, "M10")
    M25 = (0.25, 2, "M25")
    M50 = (0.50, 3, "M50")
    M100 = (1.00, 4, "M100")
    
    def __init__(self, value, volume, label):
        self._value = value
        self._volume = volume
        self._label = label
    
    def getLabel(self) -> str:
        return self._label
    
    def getValue(self) -> float:
        return self._value

    def getVolume(self) -> int:
        return self._volume

    def __str__(self):
        return f"{self._label}:{self._value:.2f}:{self._volume}"
    
class Item(Valuable):
    def __init__(self, label: str, volume: int, value: float):
        self.label = label
        self.volume = volume
        self.value = value
    
    def getLabel(self) -> str:
        return self.label

    def getValue(self) -> float:
        return self.value

    def getVolume(self) -> int:
        return self.volume

    def setLabel(self, label: str):
        self.label = label

    def setVolume(self, volume: int):
        self.volume = volume
    
    def __str__(self):
        return f"{self.label}:{self.value:.2f}:{self.volume}"
    
class Pig:
    def __init__(self, volumeMax: int):
        self.volumeMax = volumeMax
        self.broken = False
        self.valuables = []
    
    def addValuable(self, valuable: Valuable) -> bool:
        if self.broken:
            print("fail: the pig is broken")
            return False
        
        if self.getVolume() + valuable.getVolume() > self.volumeMax:
            print("fail: the pig is full")
            return False
        
        self.valuables.append(valuable)
        return True
    
    def breakPig(self) -> bool:
        self.broken = True
        return True
    
    def getCoins(self) -> list:
        if not self.broken:
            print("fail: you must break the pig first")
            return []
  
        coins = [v for v in self.valuables if isinstance(v, Coin)]
        self.valuables = [v for v in self.valuables if not isinstance(v, Coin)]
        return coins
    
    def getItems(self) -> list:
        if not self.broken:
            print("fail: you must break the pig first")
            return []
    
        items = [v for v in self.valuables if isinstance(v, Item)]
        self.valuables = [v for v in self.valuables if not isinstance(v, Item)]
        return items
    
    def calcValue(self) -> float:
        total = 0.0
        for v in self.valuables:
            total += v.getValue()
        return total
    
    def getVolume(self) -> int:
        if self.broken:
            return 0
        total = 0
        for v in self.valuables:
            total += v.getVolume()
        return total
    
    def getVolumeMax(self) -> int:
        return self.volumeMax

    def isBroken(self) -> bool:
        return self.broken

    def __str__(self):
        lista_str = "[" + ", ".join(str(v) for v in self.valuables) + "]"
        
        state = "broken" if self.broken else "intact"
        valor = self.calcValue()
        vol = self.getVolume()
        
        return f"{lista_str} : {valor:.2f}$ : {vol}/{self.volumeMax} : {state}"

def main():
    pig = Pig(0)

    while True:
        try:
            line = input()
        except EOFError:
            break
        except Exception:
            break
        
        if not line:
            continue

        print("$" + line)
        args = line.split(" ")

        if  args[0] == "end":
            break
        elif  args[0] == "init":
            pig = Pig(int(args[1]))
        elif  args[0] == "show":
            print(pig)
        elif  args[0] == "addCoin":
            valor = int(args[1])
            if valor == 10:   pig.addValuable(Coin.M10)
            elif valor == 25: pig.addValuable(Coin.M25)
            elif valor == 50: pig.addValuable(Coin.M50)
            elif valor == 100: pig.addValuable(Coin.M100)
        
        elif args[0] == "addItem":
             label = args[1]
             value = float(args[2])
             volume = int(args[3])
             item = Item(label, volume, value)
             pig.addValuable(item)
        
        elif args[0] == "break":
             pig.breakPig()
        elif args[0]  == "extractCoins":
             if pig.isBroken():
                 print("[" + ", ".join(str(c) for c in pig.getCoins()) + "]")
             else:
                 pig.getCoins()
        elif args[0] == "extractItems":
             if pig.isBroken():
                 print("[" + ", ".join(str(i) for i in pig.getItems()) + "]")
             else:
                 pig.getItems()


main()

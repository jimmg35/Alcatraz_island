import hashlib

class Key():
    def __init__(self, data: str): # Setter function
        self.__data = hashlib.sha256(data.encode('utf-8')).hexdigest()

    def insertKey(self):  # Getter function
        return self.__data


class Vehicle():
    def __init__(self, types: str, purpose: str):
        self.__type: str = types
        self.__purpose:str = purpose
        self.__engineStatus: bool = False
    
    def switchEngine(self, key: Key) -> None:
        self.__engineStatus = not self.__engineStatus

    def getEngineStatus(self):
        return self.__engineStatus


class Car(Vehicle):
    def __init__(self, brand: str, model: str, key: Key):
        super().__init__("Land", "Domestic")
        self.__brand: str = brand
        self.__model: str = model
        self.__startCode: str = key.insertKey()
    
    def checkKey(self, key: Key) -> bool:
        if key.insertKey() == self.__startCode:
            return True
        else:
            return False

    def switchEngine(self, key: Key) -> None:  #python 不支援多載
        if self.checkKey(key):
            super().switchEngine(key)
        else:
            print("You pick the wrong key!")
    
    def go(self):
        if self.getEngineStatus():
            print("GOGOGO!~")
        else:
            print("The engine hasn't been started!")



if __name__ == '__main__':
    myKey: Key = Key("ThisIsMyKey")
    myCar: Car = Car("Mercedes-benz", "CLA250", myKey)
    
    myCar.go()

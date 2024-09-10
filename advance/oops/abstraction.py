from abc import ABC, abstractmethod

class animal(ABC):
    @abstractmethod
    def voice(self):
        pass

class dog(animal):
    def voice(self):
        return "Woof!"
    
class cat(animal):
    def voice(self):
        return "Meow!"
    
# obj = animal()

obj = dog()

print(obj.voice())

obj = cat()

print(obj.voice())
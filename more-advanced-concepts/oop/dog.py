class Dog:
    __slots__ = ['__name', '__age', '__race']    
    
    def __init__(self, name: str, age: int=None, race: str=None):
        self.__name = name
        self.__age = age
        self.__race = race        

    def __repr__(self):
        if self.__age == None and self.race == None:
            return self.name
        elif self.__age == None:
            return f"{self.name}, dog of race {self.race}"            
        elif self.__race == None:
            return f"{self.name}, {self.age} years old dog"
        else:
            return f"{self.name}, {self.age} years old {self.race}"
        
    def get_name(self):
        return self.__name
    
    def change_name(self, new_name):
        self.__name = new_name
    
    def get_age(self):
        return self.__age
    
    def get_race(self):
        return self.__race
    
    name = property(get_name, change_name)
    age = property(get_age)
    race = property(get_race)
        
    def bark(self):
        print("WOOF!")    
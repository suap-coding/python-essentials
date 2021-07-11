from typeguard import typechecked

class Dog:
    __slots__ = ['__name', '__age', '__race']    
    
    @typechecked
    def __init__(self, name: str, age: int=None, race: str=None) -> None:
        self.__name = name
        self.__age = age
        self.__race = race        

    def __repr__(self) -> str:
        if self.__age == None and self.race == None:
            return self.name
        elif self.__age == None:
            return f"{self.name}, dog of race {self.race}"            
        elif self.__race == None:
            return f"{self.name}, {self.age} years old dog"
        else:
            return f"{self.name}, {self.age} years old {self.race}"
        
    def get_name(self) -> str:
        return self.__name
    
    @typechecked
    def change_name(self, new_name: str) -> str:
        self.__name = new_name
        return self.__name
    
    def get_age(self) -> int:
        return self.__age
    
    def get_race(self) -> str:
        return self.__race
    
    name = property(get_name, change_name)
    age = property(get_age)
    race = property(get_race)
        
    def bark(self) -> None:
        print("WOOF!")
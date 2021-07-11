from dog import Dog
from typing import Literal
# from typeguard import typechecked

class Person:
    __slots__ = ['__name', '__age', '__gender', '__partner', '__nr_of_kids', '__dog']
    
    genders = Literal['male', 'female', 'other']
    # @typechecked
    def __init__(self, name: str, age: int=None, gender: genders=None, partner=None, nr_of_kids: int=None):
        if partner != None:
            assert type(partner) == Person
        self.__name = name
        self.__age = age
        self.__gender = gender
        self.__partner = partner
        self.__nr_of_kids = nr_of_kids

    def is_hot(self):
        if self.__gender == None:
            return False
        elif(self.__gender == 'female'):
            return 17 <= self.__age < 60
        else:
            return False
        
    def is_handsome(self):
        if self.__gender == None:
            return False
        elif(self.__gender == 'male'):            
            return 20 <= self.__age < 80
        else:
            return False
    
    # @typechecked
    def assign_dog(self, dog: Dog):
            self.__dog = dog
        
    def get_dog(self):
        return self.__dog
    
    # @typechecked
    def assign_partner(self, partner):
        assert type(partner) == Person
        self.__partner = partner
    
    def get_partner(self):
        return self.__partner
    
    dog = property(get_dog, assign_dog)
    partner = property(get_partner, assign_partner)

    def __repr__(self):
        repr = self.__name
        if self.__age != None:
            repr += f", age {self.__age}"
        if self.is_hot():
            repr += ", hot"
        elif self.is_handsome():
            repr += ", handsome"
        return repr
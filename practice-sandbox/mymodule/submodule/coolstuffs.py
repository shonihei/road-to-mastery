__author__ = "Sho Nihei"

class Person:
    def __init__(self, name, age=20, is_male=True):
        self.name = name
        self.age = age
        self.is_male = is_male
        self.relatives = dict()
        
    def __str__(self):
        return self.name

    def __repr__(self):
        return "Person('{}')".format(self.name)
    
    def add_relative(self, other_person):
        if other_person.name not in self.relatives:
            self.relatives[other_person.name] = other_person
            return True
        return False

    def is_related_to(self, other_person):
        return True if other_person.name in self.relatives else False

'''
nci programme: BSHDS 
program: toy system
author: Renato Gusani
studentID: x19411076
date: 11/04/2020

'''
class Toys:
    def __init__(self, name, category, cost):
        self.name = name 
        self.category = category
        self.cost = cost


    def __repr__(self):
            return '({}, {}, {})'.format(self.name, self.category, self.cost)


t1 = Toys("He-man","Action Figure", 3.99)
t2 = Toys("Tonka","Cars and radio controlled", 5.99)
t3 = Toys("Lego","Construction toys", 9.99)
t4 = Toys("Play-Doh","Creative Toys", 0.99)
t5 = Toys("Ant Farm","Educational Toys", 1.99)

allToys= [t1, t2, t3, t4, t5]

def sortallToys_name(allig):
    return allig.name

def sortallToys_category(allig):
    return allig.category

def sortallToys_cost(allig):
    return allig.cost


sorted_allToys_name= sorted(allToys, key= sortallToys_name)
sorted_allToys_category= sorted(allToys, key= sortallToys_category)
sorted_allToys_cost= sorted(allToys, key= sortallToys_cost)

print(allToys) # prints all toys

print("Toys sorted by name:", sorted_allToys_name) # prints all toys by name 
print("Toys sorted by category:", sorted_allToys_category) # prints all toys by category
print("Toys sorted by cost:", sorted_allToys_cost) # prints all toys by cost low to high
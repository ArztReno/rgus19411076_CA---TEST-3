'''
nci programme: BSHDS 
program: mass system
author: Renato Gusani
studentID: x19411076
date: 12/04/2020

'''
class mass:
    def __init__(self, name, height_m, weight_kg):
        self.name = name 
        self.height_m = height_m
        self.weight_kg = weight_kg

p1 = mass("James Bond", 1.8, 90)
p2 = mass("Lara Croft", 1.8, 70)


def mass(name, height_m, weight_kg):
  bmi = weight_kg / (height_m ** 2)
  print("mass: ")
  print(mass)
  if mass < 25:
    return name + " is light"
    elif:
      return name + " is heavy"

    result1 = mass(p1)
    result2 = mass(p2)

 # del p1
 # del p2
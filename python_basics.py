#!/bin/python3

name = input("Enter name?")
age = int(input("Enter age?"))
degree = input("Enter degree program?")
remaining_age = (age * 3) % 2
print (name, age, degree, str(remaining_age))



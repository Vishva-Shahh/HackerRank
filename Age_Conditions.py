
import math
import os
import random
import re
import sys



N = 18
print("Weird" * ((N % 2 != 0) or ((N % 2 == 0) and (N in range(6, 21)))) +
      "Not Weird" * ((N % 2 == 0) and ((N in range(2, 6)) or (N > 20))))


class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAgex`
        if initialAge < 0:
            self.age = 0
            print("Age is not valid, setting age to 0.")
        else:
            self.age = initialAge

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print("You are young.")
        elif 13 <= self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def yearPasses(self):
        # Increment the age of the person in here
        self.age += 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")


"""
Author: zhiwei_199
Time: 2022/08/29
Theme: if
"""

from tokenize import String


def ifStudy():
    cars = ['bmw', 'audi', 'benz']
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())
    other_car = 'yage'
    if other_car not in cars:
        print("not in")

def ifStudy2():
    age = 11
    if age > 5 and age < 10:
        print("bigger")
    elif age < 5 and age > 0:
        print("equals")
    elif age > 10 or age < 15:
        print("bigger and bigger")
    else:
        print("none")
    
if __name__=="__main__":
    #ifStudy()
    ifStudy2()
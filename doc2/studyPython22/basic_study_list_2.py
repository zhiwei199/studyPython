"""
Author: zhiwei_199
Time: 2022/08/28
Theme: list
"""
def listStudy2():      
    cars = ['bmw', 'audi', 'benz']
    cars.sort()    #根据字母正序排序，该修改为永久性
    print(cars)

def listStudy2_1():
    cars = ['bmw', 'audi', 'benz']
    cars.sort(reverse=True)   #逆序排序
    print(cars)

def listStudy2_2():
    #临时排序,不改变列表原始排序
    cars = ['bmw', 'audi', 'benz']
    print(sorted(cars))
    print(cars)

def listStudy2_3():
    cars = ['bmw', 'audi', 'benz']
    cars.reverse()   #反转列表排序，永久性，区分于sort(reverse=True)
    print(cars)
    print(len(cars))   #获取列表长度
    print(cars[-1])   #获取列表最后一个元素

def operateList2():
    cars = ['bmw', 'audi', 'benz']
    for car in cars:
        print(car.title() + ", is so beautiful!")

def operateList2_1():
    #for value in range(1, 5):   #创建数值列表，5时停止
        #print(value)
    #numbers = list(range(1, 5))
    #print(numbers)
    even_numbers = list(range(1, 10, 3))   #设置步长为3
    print(even_numbers)
    #将前10个数的平方加入列表
    #方法一
    squares = []
    for value in range(1, 11):
        square = value ** 2
        squares.append(square)
    print(squares)
    #squares = [value ** 2 for value in range(1, 11)]
    #print(squares)

if __name__=="__main__":
    #listStudy2()
    #listStudy2_1()
    #listStudy2_2()
    #listStudy2_3()
    #operateList2()
    operateList2_1()
def listStudy():
    first_list = ['one', 'two', 'three', 'four']
    print(first_list[0])
    #add to the end of list
    first_list.append('five')
    print(first_list)
    #insert to the definte location
    first_list.insert(0, 'zero')
    print(first_list)
    #delete by the index
    del first_list[0]
    print(first_list)
    #pop() delete the end of the list and take it out
    second_list_1 = ['time', 'life', 'work']
    pop_0_second_list = second_list_1(0)
    print(second_list_1)
    print(pop_0_second_list)
    
if __name__=="__main__":
    listStudy()

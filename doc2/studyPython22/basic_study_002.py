from email import message

def printHelloWorld():
    message = "Hello Python World!"
    print(message)
    message = "hello Crash World!"
    print(message.title())
    name = "hello Magic Python World!"
    second_name = "Its so fun!"
    print(name.title())  #����ĸ��Ϊ��д
    print(name.upper())  #ȫ����Ϊ��д
    print(name.lower())  #ȫ����ΪСд��ת���󷽱�洢
    print("Hello World!")
    full_name = name + " " + second_name
    print(full_name)
    print("\nPython\nSoFun")

    first_message = 'Python   '
    #ȥ��ĩβ�հ�
    print(first_message.rstrip() + "show") 
    print(first_message + "show")
    #��ȥ���հ����ô���ԭ����
    #first_message = first_message.rstrip()
    #print(first_message)


if __name__=="__main__":
    printHelloWorld()

    



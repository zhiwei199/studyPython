from email import message

def printHelloWorld():
    message = "Hello Python World!"
    print(message)
    message = "hello Crash World!"
    print(message.title())
    name = "hello Magic Python World!"
    second_name = "Its so fun!"
    print(name.title())  #首字母变为大写
    print(name.upper())  #全部变为大写
    print(name.lower())  #全部变为小写，转化后方便存储
    print("Hello World!")
    full_name = name + " " + second_name
    print(full_name)
    print("\n\tPython\nSoFun")

    first_message = 'Python   '
    #去除末尾空白
    print(first_message.rstrip() + "show") 
    print(first_message)
    #将去除空白永久存入原变量
    #first_message = first_message.rstrip()
    #print(first_message)


if __name__=="__main__":
    printHelloWorld()

    



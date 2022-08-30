"""
Author: zhiwei_199
Time: 2022/08/29
Theme: dictionary
"""
def dictionaryStudy():
    player_p = {'player': 'curry', 'points': 'three'}
    print(player_p['player'])    # 字典值使用方法
    print(player_p['points'])   # 字典名['key'] 调用值

def dictionaryStudy2():
    player_0 = {}       # 创建空字典
    player_0['player'] = 'james'     # 赋值
    player_0['points'] = 'two'
    #print(player_0)
    # 修改键值, 赋予键新的值
    player_0['player'] = 'green'
    print(player_0)
# 遍历字典
def dictionaryStudy3():
    user = {
        'username': 'curry',
        'first': 'two',
        'second': 'three'
    }  # key, value 可用其他任意变量名替换，使语句更易懂
    for key, value in user.items():  # items()方法，返回一个键-值对列表
        print("\nkey: " + key)  #  '\n'插入空行
        print("value: " + value)

# 遍历字典中的键, 使用 keys() 方法
def dictionaryStudy4():
    prefer_languages = {
        'curry': 'python', 
        'james': 'c',
        'green': 'go',
        'jordon': 'ruby'
    }
    if 'klay'  not in prefer_languages.keys():
        print("He is not in")
    friends = ['curry', 'klay']
    for name in prefer_languages:     # 遍历字典，默认遍历所有键
        print(name.title())
    for name in prefer_languages.keys():
        print(name.title())
        if name in friends:
            print(name.title() + "'s favorite languages is " 
            + prefer_languages[name].title())

def dictionaryStudy5():
    prefer_languages = {
        'curry': 'python', 
        'james': 'c',
        'green': 'go',
        'jordon': 'ruby',
        'klay': 'python'
    }   #  顺序遍历字典中的键sorted()
    #for name in sorted(prefer_languages.keys()):
        #print(name.title())
    #  遍历字典中的值values()
    for language in prefer_languages.values():
        print(language.title())
    # 剔除重复项set()
    print("the following is about set()")
    for language in set(prefer_languages.values()):
        print(language.title())

"""
new part: 嵌套
"""
def dictionaryStudy6():
    players = []
    for player_number in range(30):
        new_player = {'clothes': 'blue',
        'points': 'three',
        'hight': '190'
        }
        players.append(new_player)
    for player in players[:5]:
        print(player)
    print(str(len(players)))

if __name__=="__main__":
    #dictionaryStudy()
    #dictionaryStudy2()
    #dictionaryStudy3()
    #dictionaryStudy4()
    #dictionaryStudy5()
    dictionaryStudy6()



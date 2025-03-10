#计算字符串的长度
def len_wyz(str):
 count=0
 for i in str:
    count+=1
 print(f"{str} is {count}")

wyz="sjiwiwi"
len_wyz(wyz)
#嵌套函数
def funa():
    a=1
    return a
def funb():
    b=2
    return b
def func():
    c=funa()+funb()
    print(c)
func()

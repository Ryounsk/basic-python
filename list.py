#index:查找元素下标,如果不存在会报错
wyzlist=["wyz","llz","wsj"]
index=wyzlist.index("wsj")
print(index)
#insert
wyzlist.insert(1,"kk")
print(wyzlist)
#append:在尾部追加元素
wyzlist.append("ss")
#extend:尾部追加一批元素
list2=[1,2,3]
wyzlist.extend(list2)
#del list[下标]
del wyzlist[1]
#pop：先取出元素
element=wyzlist.pop[4]
wyzlist.remove("wyz")
#清空列表
wyzlist.clear()
#count:统计重复元素
list1=[1,2,3,33,3,5]
count=list1.count(3)
sum=len(wyzlist)
#list遍历
my_list=["111","222","wyz"]
def list_while():
    index=0
    while index<len(my_list):
        x=my_list[index]
        print("{x}")
        index+=1
def list_for():
    for x in my_list:
        print("{x}")

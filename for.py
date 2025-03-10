"""
eg:
name="12345678"
for x in name:
    print(x,end='')
"""
#定义一个变量，用来统计有多少个w
count=0
name="wyz is alo in the world"
#for 循环统计
#for 临时变量in 被统计的数据
for x in name:
    if x == "w":
        count +=1
print(f"have{count}w")

#range 语句
range(3,7)
range(7)
for x in range(2,8,2):
    print (x)

#for循环嵌套

for i in range(1,10):
    #内循环
    for j in range(i):
        print(f"{j+1}*{i}={(j+1)*i}\t",end='')

    print()
#continue嵌套试用
for i in range(1,10):
    print(555)
    for j in range(i):
        print(f"{j+1}*{i}")
        continue
        #我觉得continue跟break的差别就是前者跳过一个回合，后者跳过后面所有回合
        print(666)
    print(777)
#break使用
name ="wyzllzwsj"
for i in name:
    if i=='l':
        break
    print (i)




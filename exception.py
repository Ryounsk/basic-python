#基本捕获异常语法
try:
    f=open("python.txt","r",encoding="UTF-8")
except:
    print("出现异常，文件不存在")
    #改用w方式打开
    f = open("python.txt", "w", encoding="UTF-8")
#捕获多个异常
try:
    print(1/0)
except(NameError,ZeroDivisionError)as e:
    print('多个错误')
#捕捉所有的异常
try:
    print(1/0)
except Exception as e:
    print("出现异常")
#else
else:
    print("no have exception")
#finally无论如何都会运行
finally:
    f.close()


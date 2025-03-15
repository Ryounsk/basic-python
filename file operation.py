#open(name,mode,encoding),r是读，w是写，a是追加写入
import time

f=open('python.txt','r+w+a',encoding='UTF-8')
#read方法
print(f"{f.read(10)}")#读取十个字节，空括号是读取全部
#readlines方法:读取文件所有行封装成列表
#只要文件打开后，每一次读取都会续接上一次读取方法读取到的位置
#for循环读取
for line in f:
    print(f"{line}")
#暂停程序
time.sleep(500)#暂停500秒
#文件关闭
f.close()
#with open语法操作文件运行可以自动关闭文件
#f.flush 把积攒的内容写入，不调用flush,直接调用close也有这个方法作用
#write方法写入
f.write("wyz&wsj")

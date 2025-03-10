#定义外层循环的控制变量
i=1
while i<=9:

#定义内层循环的控制变量
      j=1
      while j<=i:
          #内层循环的print语句不换行
          print(f"{j}*{i}={j*i}\t",end='')
          j+=1
      i+=1
      print()


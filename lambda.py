#匿名函数，只能用一次
def test_func(computer):
    result=computer(1,2)
    print(f"{result}")
test_func(lambda x,y:x+y)
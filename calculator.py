def sum(a,b):#加法
    return a+b
def jian(a,b):#减法
    return a-b
def mul(a,b):#乘法
    return a*b
def tri(a,b):#除法
    return a/b

while True:
    print(
    """"
    ===== 计算器 =====
1. 加法
2. 减法
3. 乘法
4. 除法
0. 退出
请输入选项：
    
    """
)
    try:
        choice = int(input("请输入你要使用的算法:"))
    except:
        print("输入错误，请输入数字")
        continue
    match choice:
        case 0:
            print("退出计算机")
            break
        case 1:
            a=int(input("请输入第一位数字:"))
            b=int(input("请输入第2位数字:"))
            result=sum(a,b)
            print("计算结果:",result)
        case 2:
            a=int(input("请输入第一位数字:"))
            b=int(input("请输入第2位数字:"))
            result=jian(a,b)
            print("计算结果:",result)
        case 3:
            a=int(input("请输入第一位数字:"))
            b=int(input("请输入第2位数字:"))
            result=mul(a,b)
            print("计算结果:",result)
        case 4:
            a=int(input("请输入第一位数字:"))
            b=int(input("请输入第2位数字:"))
            if b==0:
                print("除数不能为 0")
                continue
            result=tri(a,b)
            print("计算结果:",result)
        case _:
            print("非法操作,请重新输入")
            continue
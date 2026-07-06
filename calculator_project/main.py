from math_utils import *
from utils import *
def run():
    while True:
        show_menu()
        choice=int(get_number("请输入选项"))
        match choice:
            case 0:
                print("退出计算机")
                break
            case 1:
                a=get_number("请输入第一位数字:")
                b=get_number("请输入第二位数字:")
                result=sum(a,b)
                print("计算结果:",result)
            case 2:
                a=get_number("请输入第一位数字:")
                b=get_number("请输入第二位数字:")
                result=jian(a,b)
                print("计算结果:",result)
            case 3:
                a=get_number("请输入第一位数字:")
                b=get_number("请输入第二位数字:")
                result=mul(a,b)
                print("计算结果:",result)
            case 4:
                a=get_number("请输入第一位数字:")
                b=get_number("请输入第二位数字:")
                if b==0:
                    print("除数不能为 0")
                    continue
                result=tri(a,b)
                print("计算结果:",result)
            case _:
                print("非法操作,请重新输入")
                continue

run()
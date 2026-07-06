def show_menu():
    print(
        """
        ===== 计算器 =====
    1. 加法
    2. 减法
    3. 乘法
    4. 除法
    0. 退出
    请输入选项：
        
        """
    )

def get_number(message):
    while True:
        try:
            num = float(input(message))
            return num
        except:
            print("输入错误，请输入数字")
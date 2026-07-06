import random


def show_menu():
    print(
        """
===== 猜数字游戏 =====
系统会生成 1~100 的数字
请输入你猜的数字
"""
    )


def generate_number():
    return random.randint(1, 100)


def get_user_guess():
    while True:
        try:
            guess = int(input("请输入你猜测的数字:"))
        except:
            print("输入错误，请输入数字")
            continue

        if guess > 100 or guess < 1:
            print("超过范围，请输入 1~100 的数字")
            continue

        return guess


def check_guess(answer, guess):
    if guess > answer:
        print("猜大了")
        return False
    elif guess < answer:
        print("猜小了")
        return False
    else:
        print("恭喜你，猜对了!!!")
        return True


def run_game():
    show_menu()

    answer = generate_number()
    count = 0

    while True:
        guess = get_user_guess()
        count += 1

        is_right = check_guess(answer, guess)

        if is_right:
            print("你一共猜了", count, "次")
            break


run_game()
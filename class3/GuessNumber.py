import random
sys_num = random.randint(1, 1000)
while True:
    user_num = input("请输入一个1-1000的整数：")
    try:
        user_num = int(user_num)
        if user_num < 1 or user_num > 1000:
            print("数字超出范围，请重新输入！")
            continue
        if user_num == sys_num:
            print("恭喜你，中奖啦！")
            break
        elif user_num < sys_num:
            print("猜小了")
        else:
            print("猜大了")
    except ValueError:
        print("输入的不是整数，请重新输入！")
import random

# 功能1：生成一个1~10的幸运数字
lucky_number = random.randint(1, 10)
print(f"你的幸运数字是：{lucky_number}")

# 功能2：生成3个1~10的随机数字
a = random.randint(1, 10)
b = random.randint(1, 10)
c = random.randint(1, 10)
print(a)
print(b)
print(c)

# 功能3：判断有没有中奖
if a == lucky_number or b == lucky_number or c == lucky_number:
    print("恭喜你，中奖了！")
else:
    print("很遗憾，没中奖，下次再试！")

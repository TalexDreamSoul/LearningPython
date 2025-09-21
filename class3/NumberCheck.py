num = input("请输入一个整数:")
try:
    num = int(num)
    if num%2==0 and num%3 == 0:
        print("Yes")
    else:
        print("No")
except ValueError:
    print("输入的不是整数，请重新输入!")
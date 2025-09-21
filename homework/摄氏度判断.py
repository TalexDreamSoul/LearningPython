def temp_convert():
    temp = input("请输入带符号的温度值(如32C或67F)：").strip()
    if len(temp) < 2:
        print("输入格式不正确！")
        return

    value, unit = temp[:-1], temp[-1]
    try:
        value = float(value)
    except ValueError:
        print("温度数值格式错误！")
        return

    if unit in ['C', 'c']:
        f = value * 1.8 + 32
        print(f"转换后的温度是 {f:.2f}F")
    elif unit in ['F', 'f']:
        c = (value - 32) / 1.8
        print(f"转换后的温度是 {c:.2f}C")
    else:
        print("输入的温度单位无效，请使用C或F！")

# 调用函数
temp_convert()

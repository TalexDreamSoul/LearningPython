pm25 = input("请输入今日的PM2.5值：")
try:
    pm25 = float(pm25)
    if pm25 <= 35:
        print("空气质量：优")
    elif 35 < pm25 <= 75:
        print("空气质量：良")
    else:
        print("空气质量：污染")
except ValueError:
    print("输入的不是有效数字，请重新输入！")
def express_fee():
    length = float(input("请输入包裹的长度(m): "))
    width  = float(input("请输入包裹的宽度(m): "))
    height = float(input("请输入包裹的高度(m): "))
    weight = float(input("请输入包裹的重量(kg): "))

    # 判断是否可以快递
    if length > 1 or width > 1 or height > 1 or weight > 40:
        print("抱歉，该包裹尺寸或重量超标，不予快递。")
        return

    # 基本手续费
    fee = 5.0

    # 按重量计算运费
    if weight < 10:
        fee += 1.5
    elif weight < 30:
        fee += 2.0
    else:  # 30 <= weight < 40
        fee += 2.5

    print(f"您邮寄的包裹所需邮资为 {fee:.1f}元")

# 调用函数
express_fee()

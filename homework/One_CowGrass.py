def grass_growth(cows1, days1, cows2, days2):
    """
    cows1, days1: 第一组条件 (多少头牛能吃多少天)
    cows2, days2: 第二组条件 (多少头牛能吃多少天)
    返回每天新生草量可供几头牛吃一天
    """
    # 两个方程：
    # S + days1 * x = cows1 * days1
    # S + days2 * x = cows2 * days2

    total1 = cows1 * days1
    total2 = cows2 * days2

    # 相减消元 S
    x = (total1 - total2) / (days1 - days2)
    return int(x)

# 题目中的数据
print("每天新生的草量可供", grass_growth(15, 20, 20, 10), "头牛吃1天")

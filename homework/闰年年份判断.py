def is_leap_year(y):
    """判断年份 y 是否为闰年"""
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

# 测试
years = [1900, 2000, 2020, 2021, 2024]
for year in years:
    print(f"{year} 年是闰年吗？{'是' if is_leap_year(year) else '否'}")

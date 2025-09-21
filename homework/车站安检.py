def yn(prompt):
    """
    统一把用户输入的 是/否 转成 True/False
    支持：是/有/y/yes/1 和 否/无/n/no/0
    """
    s = input(prompt).strip().lower()
    return s in {"是", "有", "y", "yes", "1", "true", "t"}

def read_float(prompt):
    """安全读取浮点数（厘米），失败会再次提示。"""
    while True:
        s = input(prompt).strip().replace("厘米", "").replace("cm", "").replace("CM", "")
        try:
            v = float(s)
            if v < 0:
                print("长度不能为负数，请重新输入。")
                continue
            return v
        except ValueError:
            print("请输入数字（单位：厘米），例如 9 或 12.5。")

def security_check():
    print("=== 车站安检 ===")

    # (1) 是否有车票
    has_ticket = yn("是否持有车票？(是/否)：")
    if not has_ticket:
        print("【结果】未持票，不允许进站。")
        return

    # (2) 是否携带管制刀具
    has_knife = yn("是否携带刀具？(有/无)：")
    if not has_knife:
        print("【结果】安检通过，可以上车。")
        return

    # (3) 判断刀具长度
    length_cm = read_float("请输入刀具长度（厘米）：")
    if length_cm > 10:
        print(f"【结果】刀具长度 {length_cm:.1f} cm ＞ 10 cm，不允许上车。")
    else:
        print(f"【结果】刀具长度 {length_cm:.1f} cm ≤ 10 cm，安检通过，可以上车。")

if __name__ == "__main__":
    security_check()

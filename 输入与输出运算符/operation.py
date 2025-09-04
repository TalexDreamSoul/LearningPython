# 定义theOperation方法，包括apple和pear两个参数，分别表示苹果和梨子的数量

def theOperation(apple, pear):
    # 1.请在此处填入计算苹果个数加梨的个数的代码，并将结果存入sum_result变量输出结果。

    ########## Begin ##########
    sum_result = apple + pear
    print(f"Apple + Pear = {sum_result}")

    ########## End ##########

    # 2.请在此处填入苹果个数除以梨的个数的代码，并将结果存入div_result变量，并输出结果。
    # 注意：如果 pear 为 0，会发生 ZeroDivisionError。实际应用中应进行除零判断。

    ########## Begin ##########
    if pear != 0:
        div_result = apple / pear
        print(f"Apple / Pear = {div_result}")
    else:
        print("Apple / Pear !!! 无法除以0")

    ########## End ##########

    # 3.请在此处填入苹果个数的2次幂的代码，并将结果存入exp_result变量，并输出结果。

    ########## Begin ##########
    exp_result = apple ** 2
    print(f"Apple ** 2 = {exp_result}")

    ########## End ##########

    # 4.请在此处填入判断苹果个数是否与梨的个数相等的代码，并将结果存入isequal变量，并输出结果。

    ########## Begin ##########
    isequal = apple == pear
    print(f"Apple == Pear = {isequal}")

    ########## End ##########

    # 5. 请在此处填入判断苹果个数是否大于等于梨的个数的代码，并将结果存入ismax变量，并输出结果。
    # 注意：题目要求“大于等于”，但你的代码写的是“大于”，这也算一个小的逻辑不符。

    ########## Begin ##########
    ismax = apple >= pear
    print(f"Apple >= Pear = {ismax}")

    ########## End ##########

    # 6.请在此处填入用赋值乘法运算符计算梨个数乘以2的代码，并将结果存入multi_result变量，并输出结果。

    ########## Begin ##########
    temp_pear = pear
    temp_pear *= 2
    multi_result = temp_pear
    print(f"Pear *= 2, result = {multi_result}")


########## End ##########

if __name__ == '__main__':
    apple = int(input("请输入苹果数量: "))
    pear = int(input("请输入梨数量: "))
    theOperation(apple, pear)


# 定义逻辑运算处理函数theLogic,其中tom与Jerry分别代表两个输入参数

def theLogic(tom, jerry):
    # 请在此处填入jerry的布尔“非”代码,并将结果存入到not_result这个变量

    ########## Begin ##########
    not_result = not jerry
    ########## End ##########

    print(not_result)

    # 请在此处填入tom,jerry的逻辑与代码，并将结果存入到and_result这个变量

    ########## Begin ##########
    and_result = tom and jerry
    ########## End ##########

    print(and_result)

if __name__ == '__main__':
    theLogic(5, 5)

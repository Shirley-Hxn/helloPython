def multiple_table():
    """封装函数"""
    # 外循环控制行，内循环控制列
    row = 1
    while row <=9:
        col = 1
        while col <= row:
            count = row * col
            # end = "" 结束换行输出 ； 转义字符 \t 使乘法表对齐
            print("%d * %d = %d" % (row,col,count), end = "\t")
            col += 1
        print("")  # 勿遗漏：打印行
        row += 1
# 调用封装好的函数
multiple_table()

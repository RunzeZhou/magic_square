import os
from functions import cre_empty_matrix, odd_matrix, double_even_matrix, cre_spec_matrix, single_even_matrix


print("本程序将构造一个可能的n（n>2）阶幻方.\n")

# 输入与输入检查
x = input("请输入阶数（输入-1以退出）：")
x = int(x)
while (x <= 2) and (x != -1):
    print("输入错误！请重新输入！")
    x = input("请输入阶数（输入-1以退出）：")
    x = int(x)

# 按照类型区分幻方并进行运算
if (x % 2 == 1) and (x != -1):
    matrix = odd_matrix(x)
elif x % 4 == 0:
    matrix = double_even_matrix(x)
elif x % 4 == 2:
    matrix = single_even_matrix(x)
else:
    matrix = cre_empty_matrix(1)

# 输出幻方
if len(matrix) != 1:
    print(f"\n所构造的{x}阶幻方为：")
    for i in range(0, x):
        print(matrix[i])
print("\n程序结束！")

os.system("pause")

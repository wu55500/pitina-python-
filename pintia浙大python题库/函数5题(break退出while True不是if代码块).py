# 第6章函数 - 5
# 使用函数求余弦函数的近似值
# 本题要求实现一个函数，用下列公式求cos(x)
# 近似值，精确到最后一项的绝对值小于eps（绝对值小于eps的项不要加）：
# 函数接口定义：funcos(eps, x), 其中用户传入的参数为eps和x；函数funcos应返回用给定公式计算出来，保留小数4位。
# 函数接口定义：
# 函数接口:
# funcos(eps, x), 返回cos(x)
# 的值。
# 裁判测试程序样例：
# 在这里给出函数被调用进行测试的例子。例如：
# # 输入样例
# eps, x = input().split()
# eps, x = float(eps), float(x)
# value = funcos(eps, x)
# print("cos({0}) = {1:.4f}".format(x, value))
# 输入样例：
# 0.0001 - 3.1
# 输出样例：
# cos(-3.1) = -0.9991
from functools import reduce
print(reduce(lambda x,y:x*y, range(1,11)))  # 计算1到10的乘积

#如果 eps = 0.0001，那么当某一计算项（如 、 等）的绝对值小于 0.0001 时，就不再累加这一项，认为结果已经足够精确。
# 如果 eps 的值更大（如 0.01），计算过程会更快终止，但结果的精度可能不如 eps 更小时高。
def funcos(eps, x):
    cos = 0.0
    n = 0
    while True:
        分子 = 1
        for i in range(1, 2 * n + 1):
            分子 *= i
        term=((-1)**n)*(x**(2*n))/分子
    #以上代码可简化为推导式子return ((-1)**n * x**(2*n) / factorial(2*n) for n in range(max_n))
        if abs(term) < eps:         #如果当前项的绝对值小于eps，停止循环
            break   #break在这段代码中的作用是退出while True循环
        cos+= term
        n += 1
    return round(cos, 4)  # 保留4位小数
eps,x=0.0001,-3.1
value=funcos(eps,x)
print("cos({0}) = {1:.4f}".format(x,value))

#将以上代码拆分成2段def,不使用任何库函数
from functools import reduce
def 分子用传参(n):
    """计算n的阶乘"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def funcos(eps, x):
    cos = 0.0
    n = 0
    while True:
        term = ((-1)**n) * (x**(2*n)) /分子用传参(n)
        if abs(term) < eps:  # 如果当前项的绝对值小于eps，停止循环
            break
        cos += term
        n += 1
    return round(cos, 4)  # 保留4位小数
eps, x = map(float, input('输入2数').split())
value = funcos(eps, x)
print("cos({0}) = {1:.4f}".format(x, value))

#改写以上代码
# def 分子用传参(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
def funcos(eps, x):
    cos = 0.0
    n = 0
    while True:
        分子用传参=reduce(lambda x,y:x*y, range(1,n+1)) if n > 0 else 1#if n > 0 else 1是一个条件表达式(三元运算符),它之所以不会报错是因为：
#推导式后面的if n > 0 else 1含义
# #当 n = 0 时：
# range(1, 0+1) 会产生空序列 range(1,1)（空迭代器）
# reduce() 对空序列会抛出 TypeError（除非提供初始值）
# 通过 else 1 避免了这种情况，当 n=0 时直接返回 1
# 数学意义：
# 0! = 1（0的阶乘定义为1）
# 这段代码实际上是在计算 n!（n的阶乘）
# 当 n=0 时直接返回 1 既符合数学定义，又避免了程序错误
# 所以这个条件表达式是必要的，它处理了 n=0 的特殊情况，保证了程序的正确性。
        term = ((-1)**n) * (x**(2*n)) /分子用传参
        if abs(term) < eps:  # 如果当前项的绝对值小于eps，停止循环
            break
        cos += term
        n += 1
    return round(cos, 4)  # 保留4位小数
eps, x = map(float, input('输入2数').split())
value = funcos(eps, x)
print("cos({0}) = {1:.4f}".format(x, value))

#法2使用生成器方法做题

def funcos(eps, x):
    n=0
    while True:
        分子用传参 = reduce(lambda x, y: x * y, range(1, n + 1)) if n > 0 else 1
        每一项=((-1)**n)*(x**(2*n)) / 分子用传参
        n+=1
        yield f累加(每一项)
def f累加(每一项):
    global cos
    cos+=每一项
    if abs(cos)<eps:

cos=0.0
eps, x = map(float, input('输入2数').split())
value = funcos(eps, x)
print("cos({0}) = {1:.4f}".format(x, value))


import math
def funcos(eps, x):
    if eps <= 0:
        raise ValueError("eps 必须是一个正数")
    cos_value = 0  # 初始化cos(x)的值
    k = 0  # 初始化项的次数
    term = 1  # 初始化项的值
    while abs(term) >= eps:
        cos_value += term  # 累加当前项
        k += 2  # 增加次数
        term = (-1) ** (k // 2) * (x ** k / math.factorial(k))#math.factorial(k)：计算k的阶乘（k!）
    return round(cos_value, 4)  # 返回cos(x)的值，保留小数点后4位=
eps, x = map(float, input().split())
value = funcos(eps, x)
print("cos({0}) = {1:.4f}".format(x, value))

#改写代码用2个方法，法1必须用2个def，法2必须用到2层嵌套函数。2个方法必须用到生成器和迭代器yield

# 基本语法结构（法1）
def f传(x):  # 外层生成器写循环check条件，传参给内层生成器内部计算每一项
    n = 0
    while True:
        yield f被传(x, n)  # 传参给内层生成器内部yield计算每一项
        n += 1
def f被传(x, n):  # 内层计算
    return ((-1)**n) * (x**(2*n)) / factorial(2*n)

#基本语法结构（法2）
def funcos(eps, x):      # 外层函数
    def term_gen():      # 内层生成器
        n = 0
        while True:
            yield compute_term(x, n)  # 闭包访问x
            n += 1
    # 使用生成器...(外层循环调用f内)

#自己写的(多思考)
from functools import reduce

# def funcos(eps, x):
#     n = 0
#     while True:
#         分子用传参 = reduce(lambda x, y: x * y, range(1, n + 1)) if n > 0 else 1
#         每一项 = ((-1) ** n) * (x ** (2 * n)) / 分子用传参
#         n += 1
#         yield f累加(每一项)
# #提示：在第一次调用的函数里用外层循环生成器，在第二次被调用函数中用内层循环yield生成器，并在生成器中计算每一项。
# def f累加(每一项):
#     while True:
#         global cos
#         cos += 每一项
#         if abs(每一项) < eps:
#             return cos
# cos = 0.0
# eps, x = map(float, input('输入2数').split())
# value = funcos(eps, x)
# print("cos({0}) = {1:.4f}".format(x, value))


#对以上代码修改
from functools import reduce
from typing import Generator

def term_generator(x: float) -> Generator[float, None, None]:#"""生成余弦级数的每一项"""
    n = 0
    while True:
        denominator = reduce(lambda x, y: x * y, range(1, n + 1)) if n > 0 else 1
        term = ((-1) ** n) * (x ** (2 * n)) / denominator
        yield term
        n += 1
def cosine_approximator(eps: float, x: float) -> float: #"""计算余弦值直到达到指定精度"""
    total = 0.0
    for term in term_generator(x):
        total += term
        if abs(term) < eps:
            return total
if __name__ == "__main__":
    eps, x = map(float, input('请输入精度和x值(用空格分隔): ').split())
    result = cosine_approximator(eps, x)
    print(f"cos({x}) = {result:.4f}")


from functools import reduce
#(标准答案)法1：使用2个def函数（含生成器）
def term_generator(x):#"""生成器函数，产生泰勒展开的每一项"""
    n = 0
    while True:# 计算阶乘 (2n)!，使用reduce实现
        factorial = reduce(lambda a,b: a*b, range(1, 2*n+1), 1)
        term = ((-1)**n) * (x**(2*n)) / factorial
        yield term
        n += 1
def funcos(eps, x):# """计算cos(x)的近似值""
    cos = 0.0
    for term in term_generator(x):  # 使用生成器迭代
        if abs(term) < eps:
            break
        cos += term
    return round(cos, 4)
eps, x = 0.0001, -3.1
value = funcos(eps, x)
print("cos({0}) = {1:.4f}".format(x, value))

#法2：自己写的，使用2层嵌套函数
#思路1：外层循环调用内层，内层用yield递归调用外层，就是内层yield递归调用外层，
# 外层再代入内层n+1,内层判断满足条件了就不用再次yield递归外层然后让外层n+1传参
# def f(esp,x):
#     n = 0
#     # while True:
#     n+=1
#     def f内(x,n):
#                 global 每一项
#                 分子,cos= 1,0
#                 reduce(lambda x,y:x*y, range(1,n+1)) if n > 0 else 1
#                 每一项= ((-1)**n)*(x**(2*n))/分子
#                 # 以上代码可简化为推导式子return ((-1)**n * x**(2*n) / factorial(2*n) for n in range(max_n))
#                 if abs(每一项) < eps:  # 如果当前项的绝对值小于eps，停止循环
#                     return cos
#                 cos += 每一项
#                 yield f(esp,x)
# print('输出结果',f(0.0001, -3.1))
#对上述代码修改：
from math import factorial
from functools import reduce


# def f(eps, x):
#     n = 0
#     cos = 0
#     def f内(x, n):
#         nonlocal cos
#         # 计算当前项的值
#         分子 = factorial(2 * n) if n > 0 else 1
#         当前项 = ((-1) ** n) * (x ** (2 * n)) / 分子
#         if abs(当前项) < eps:  # 如果当前项的绝对值小于eps，停止递归
#             return cos
#         cos += 当前项
#         # 递归调用外层函数，n+1
#         yield from f(eps, x, n + 1)
#     # 使用生成器迭代
#     gen = f内(x, n)
#     return next(gen, cos)
# print('输出结果:', f(0.0001, -3.1))
##2层def,不用生成器函数
def funcos(eps, x, n=0, result=0):
    def term_calculator(n):
        nonlocal x
        def factorial(m):
            return 1 if m==0 else m*factorial(m-1)
        return (-1) ** n * (x ** (2 * n)) / factorial(2 * n)
    term = term_calculator(n)
    if abs(term) < eps:
        return round(result, 4)
    return funcos(eps, x, n + 1, result + term)  # 递归调用外层函数


#思路2：外层循环for i in f内():,外层用yield调用内层，内层循环+yield递归调用外层，直到达到精度要求
from functools import reduce
from functools import reduce
import math
def f(eps, x, n=0):
    cos = 0.0
    def f内(x, n):           #def f内(x, n): 这个内部函数定义了一个生成器函数
        while True:         #去掉while True循环，外层循环 for i in f内(x, n): 将只能迭代一次
            #内层 while True 的作用：
# 无限循环产生泰勒级数的每一项（余弦函数的展开项）无限生成器实现
# 每次循环计算当前 n 对应的级数项并通过 yield 返回
# 内层循环不会自己终止，而是依靠外层函数的 if abs(i) < eps: 条件来终止整个计算过程
# 这种设计使得生成器可以无限产生项，而由外层函数决定何时停止使用这些项
            分子 = reduce(lambda a, b: a * b, range(1, 2 * n + 1), 1) if n > 0 else 1  # 修正0!的情况
            每一项 = ((-1)**n) * (x**(2*n)) / 分子
            yield 每一项       #实际创建生成器对象的是 yield 每一项 这一行
            n += 1
    for i in f内(x, n):
        if abs(i) < eps:#外层函数for i in f内()后内层while True循环返回值,
# while True循环终止条件由外层函数的if abs(i)<eps:控制,当某项的绝对值小于精度要求时,外层函数会return从而间接终止该循环。
            return cos
        else:
            cos += i
x = -3.1
print('代码计算结果:', f(0.0000001, x))  # 更小的eps提高精度
print('math.cos结果:', math.cos(x))  # 应该约等于-0.9991
#以上代码执行逻辑
# 1外层函数for i in f内()调用内层生成器函数 f内(x, n)
# 2内层生成器函数 f内(x, n)中的while True循环会通过yield语句逐个返回每一项的值，而不是一次性返回所有值
# while True作用是：
    # 生成器函数 f内(x, n) 内部的循环，直到满足某种条件（比如 n 达到最大值）
    # 每次循环都会返回一个值（即当前项的泰勒展开值）
# 3外层 for i in f内(x, n) 循环每次迭代时:
# 会从内层生成器获取一个值（即当前项的泰勒展开值）
# 这个值赋给变量 i,然后立即执行 if abs(i) < eps 的判断
# 这个过程是交替执行的:
# 外层获取一个值 → 判断 → 如果不符合条件就加到 cos 上
# 然后才会继续下一次迭代，再次触发内层生成器产生下一个值
# 当某项的绝对值小于eps时,外层函数return cos,这会终止整个计算过程,包括内层的while True循环

# 必须用2层def，内外层不用while True,如何实现外层n递增，内层能调用外层的n代入计算每一项后，用yield递归调用外层等价代替实现外层n+1的循环
def f(eps, x, n=0):
    def inner(x, n):
        global 每一项
        分子 = 1
        # 计算阶乘 (2n)!
        分子 = reduce(lambda x, y: x * y, range(1, 2 * n + 1)) if n > 0 else 1
        每一项 = ((-1) ** n) * (x ** (2 * n)) / 分子
        if abs(每一项) < eps:  # 终止条件
            return None
        return 每一项
    当前项 = inner(x, n)
    if 当前项 is None:  # 达到精度要求，停止递归
        return
    yield 当前项
    yield from f(eps, x, n + 1)  # 递归调用，n递增
for term in f(0.0001, -3.1):
    print(term)


#法2(标准答案):(用思路2)外层def用循环调用内层def，内层def用yield递归调用外层def，直到达到精度要求
from functools import reduce
def funcos(eps, x):
    """外层函数"""
    def term_generator():
        """内层生成器函数"""
        n = 0
        while True:
            # 计算阶乘 (2n)!，使用reduce实现
            factorial = reduce(lambda a, b: a * b, range(1, 2 * n + 1), 1)
            term = ((-1) ** n) * (x ** (2 * n)) / factorial
            yield term
            n += 1
    cos = 0.0
    for term in term_generator():  # 使用生成器迭代
        if abs(term) < eps:
            break
        cos += term
    return round(cos, 4)
eps, x = 0.0001, -3.1
value = funcos(eps, x)
print("cos({0}) = {1:.4f}".format(x, value))


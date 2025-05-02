# 第6章函数 - 1
# 使用函数求特殊a串数列和
# 分数
# 10
# 作者
# 陈春晖
# 单位
# 浙江大学
# 给定两个均不超过9的正整数a和n，要求编写函数fn(a, n)
# 求a + aa + aaa + +⋯+aa⋯aa(n个a）之和，fn须返回的是数列和
# 函数接口定义：fn(a, n)其中a和n都是用户传入的参数。a的值在[1, 9]范围；n是[1, 9]区间内的个位数。函数须返回级数和
# 裁判测试程序样例：
# / *请在这里填写答案 * /
# a, b = input().split()
# s = fn(int(a), int(b))
# print(s)

#学到的点:字符串拼接2种，1:用+号拼接，2:用*号拼接，3:reduce函数拼接
#递归的方法很巧妙

#拼接思路1:：
# 法1：字符串拼接法
def fn(a, n):
    total = 0
    num_str = ''
    for i in range(n):
        num_str += str(a)
        total += int(num_str)
    return total
print(fn(5, 2))
#拼接+法2：递归
print('拼接+递归:')
def fn(a, n):
    if n == 1:
        return a
    return fn(a, n-1) + int(str(a) * n)
print(fn(5, 2))

#拼接+法3：reduce
from functools import reduce
def fn(a, n):
    return reduce(lambda x, y: x + int(str(a) * y), range(1, n+1), 0)
print(fn(5, 3))

#计算思路1:法1:递归
print('递归+计算:')
def fn(a,n):
    if n==1:
        return a
    else:
        current=0
        for i in range(n):
                current=current*10+a
#所以，fn(2, 3) 的计算过程如下：
# 第一次从n=1到3,fn(2, 3)返回 return 2+(2*10+2)+((2*10+2)*10+2)=246。
# 第2次从n=1到2,fn(2, 2) 返回 return 2+(2*10+2)=24。
# 第3次从n=1到1,fn(2, 1) 返回 return 2。
# 因此，print(fn(2,3))的输出结果是246。
        return current+fn(a,n-1)
print(fn(2,3))

#思路2:法1:循环
def fn(a,n):
    y,x=0,0
    sum=0
    for i in range(n+1):
        if i==0:
            x=a*n
        else:
            y=(n-i)*a*(10**i)
            sum+=y
            continue
    return sum+x
a,b=input('输入数字a和n：').split()
print(fn(int(a),int(b)))
# 思路2:法1':用递归改写法1
def fn_recursive(a, n, i=0, sum=0):
    if i == n + 1:
        return sum
    if i == 0:
        x = a * n
    else:
        y = (n - i) * a * (10**i)
        sum += y
        x = 0
    return fn_recursive(a, n, i + 1, sum) + x
a, b = input('输入数字a和n：').split()
s = fn_recursive(int(a), int(b))
print(s)


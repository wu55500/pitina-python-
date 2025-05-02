#第6章函数-4 使用函数输出指定范围内Fibonacci数的个数
# 本题要求实现一个计算Fibonacci数的简单函数，并利用其实现另一个函数,输出两正整数m和n（0<m<n≤100000）之间的所有Fibonacci数的数目。
# 所谓Fibonacci数列就是满足任一项数字是前两项的和（最开始两项均定义为1）的数列,fib(0)=fib(1)=1。其中函数fib(n)须返回第n项Fibonacci数；函数PrintFN(m,n)用列表返回[m, n]中的所有Fibonacci数。
# 函数接口定义：
# 在这里描述函数接口。例如：
# fib(n),返回fib(n)的值
# PrintFN(m,n)，用列表返回[m, n]中的所有Fibonacci数。
# 裁判测试程序样例：
# 在这里给出函数被调用进行测试的例子。例如：
# /* 请在这里填写答案 */
# m,n,i=input().split()
# n=int(n)
# m=int(m)
# i=int(i)
# b=fib(i)
# print("fib({0}) = {1}".format(i,b))
# fiblist=PrintFN(m,n)
# print(len(fiblist))

#学到的（记得复习错题）:(i+=1 在循环所有功能写完最后写)

def fib(i):
    x,y,ls=0,1,[]
    while True:
        # x,y=0,1           #错了，不能写在循环内,每次都是0，1开始
        x,y=y,x+y
        ls.append(y)
        if i==len(ls):
            break           #break退出while True循环,执行return ls[-1]
    return ls[-1]
def PrintFN(m,n):
    x,y,ls=0,1,[]
    # if y<=n:          #用if时代码只有一次判断和赋值操作，无法生成完整的斐波那契数列。应该使用while循环来持续生成数列。
    while y<=n:        #正确写法，用while
        x,y=y,x+y       #错误：输出5而不是4,因为在判断if y>=m之前就已经计算了下一个斐波那契数
        #执行 x,y = 89,89+55=144(先计算下一个值)，然后判断144 >= m并添加到列表中,最后才检查while 144 <= n 条件
        if y>=m:
            ls.append(y)
            # x,y=y,x+y            #后开启循环,执行完所有操作后再去累加，否则会漏掉最后一个数
    return ls
m,n,i=20,100,6
b=fib(i)
print("fib({0})={1}".format(i,b))
a=PrintFN(m,n)
for i in a:
    print(i)
print(len(a))


def fib(i):
    if i == 0:
        return 0
    x,y=0,1
    for _ in range(i-1):
        x, y = y, x + y
    return y
def PrintFN(m, n):
    fib_list = []
    x, y = 0, 1
    while y <= n:
        if y>=m:
            fib_list.append(y)
        x,y=y,x+y
    return fib_list
m,n,i=map(int,input().split())
b=fib(i)
print("fib({0})={1}".format(i,b))
print(len(PrintFN(m, n)))

while y<=n:
    if y>=m:
        ls.append(y)
        x,y=y,x+y  # 这行属于if块，仅在y>=m时执行
        # 问题：如果y < m，x, y = y, x + y不会执行，导致y的值永远不变，陷入死循环。
        # 结果：代码卡在y = 1无法退出（除非初始m <= 1）
    while y<=n:        #正确写法，用while
        x,y=y,x+y       #错误：输出5而不是4,因为在判断if y>=m之前就已经计算了下一个斐波那契数
        #执行 x,y = 89,89+55=144(先计算下一个值)，然后判断144 >= m并添加到列表中,最后才检查while 144 <= n 条件
        if y>=m:
            ls.append(y)
            # x,y=y,x+y #
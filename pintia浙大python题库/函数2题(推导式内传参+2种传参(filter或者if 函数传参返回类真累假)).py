#学到的点:(推导式内传参+2种传参 1: list(filter(函数传参,range(m,n+1)),函数结构内return返回值决定是否符合filter条件，后留在列表
#                       或者2:[x for x in range(m,n+1) if 函数传参返回类真累假]))，函数内return 返回True则加入列表，返回False则不加入列表，

def prime(p):
    for i in range(int(p)+1):            #内层循环
        if int(p)%i==0:
            return False
        else:
            return True
def PrimeSum(m,n):
    if int(m)<=int(p)<int(n):
        a=list(filter(prime(p),range(m,n+1)))#外层循环
        return sum(a)
m,n,p=int(input().split())
m=int(m)
n=int(n)
print(PrimeSum(m,n))


def prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def PrimeSum(m, n, p):
    a=list(filter(prime, range(m, n + 1)))
    # a=[x for x in range(m, n + 1) if prime(x)]    #也可以这么写,if prime(x)把前面循环遍历的x都代入，如果if prime(x)：返回True，则把x加入到列表a中
                                                               #详细见if 类真:
    a = [lambda x: x for x in range(m, n + 1) if prime(x)]#也可以这么写
    return sum(a)
m, n, p = map(int, input().split())
print(PrimeSum(m, n, p))








def prime(p):
    if p < 2:  # 小于2的数不是质数
        return False
    for i in range(2, int(p**0.5)+1):  # 只需检查到平方根
        if p % i == 0:
            return False
    return True

def PrimeSum(m, n):
    primes = [x for x in range(m, n+1) if prime(x)]
    return sum(primes)

m, n = map(int, input().split())  # 只需要输入m和n
print(PrimeSum(m, n))





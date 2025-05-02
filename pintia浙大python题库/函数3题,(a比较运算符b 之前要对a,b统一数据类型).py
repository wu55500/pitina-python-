# 第6章函数-3 使用函数统计指定数字的个数
# 分数 20
# 作者 陈春晖
# 单位 浙江大学
# 本题要求实现一个统计整数中指定数字的个数的简单函数。
# CountDigit(number,digit )
# 其中number是整数，digit为[1, 9]区间内的整数。函数CountDigit应返回number中digit出现的次数。
# 函数接口定义：
# 在这里描述函数接口。例如：
# CountDigit(number,digit ),返回digit出现的次数

#学到的点（多复习）:多用推导式子, a 比较运算符 b 之前要对a,b统一数据类型，例：a=int(a),b='str',if a<=b:报错，应该写为if str(a)<=b:

def CountDigit(number,digit):
    c=0
    # for i in number:        #报错原因:count 是int 类型，不是可迭代对象，不能用for循环遍历number。
    for i in str(number):#正确写法
        # if i==digit:      #报错(输出0原因):digit被转换为整数类型,但在CountDigit函数内部,number被转换为字符串以便逐位检查。
                                    # 这意味着 digit 也需要在比较时是字符串形式，以确保类型匹配。
        if i == str(digit):##正确写法
            c+=1
        continue
    return c
number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit)
print("Number of digit 2 in "+str(number)+":",count)

def CountDigit(number,digit):
    ls=list(i for i in str(number) if i==str(digit))
    return len(ls)
number,digit=input().split()
number=int(number)
digit=int(digit)
count=CountDigit(number,digit)
print("Number of digit 2 in "+str(number)+":",count)
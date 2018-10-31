# 水仙花数是一个n为位数（n>=3) 它的每个数字的n 次幂纸盒等于它本身
# eg：1^3+5^3+3^3 = 153

# 求100~999之间所有的水仙花数
'''
def isArmstrongNumber(n):
    a = []
    t = n
    while t > 0:
        a.append(t%10)
        t /= 10

    k = len(a)
    return sum([x ** k for x in a]) == n

for x in range(100,1000):
    if isArmstrongNumber(x):
        print(x)
'''
'''
for i in range(100,1000):
    sum = 0
    temp = i
    while temp:
        sum = sum+(temp%10)**3
        temp //= 10

    if sum == i:
        print(i)
'''
#字符串方式
for i in range(100,1000):
    if i == sum(int(c)**3 for c in str(i)):
        print(i)
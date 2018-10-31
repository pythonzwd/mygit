# 0-9这10个数可以组成多少不重复的3位数

#a:1-9,b:0-9,c:0-9

count = 0
for a in range(1,10):
    for b in range(10):
        if a == b:
            continue
        for c in range(10):
            if c != a and c != b:
                count += 1
                print(a,b,c)

print('count:',count)

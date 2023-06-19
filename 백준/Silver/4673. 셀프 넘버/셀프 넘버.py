def d(n):
    result = 0
    num = str(n)
    result += n
    for i in range(len(num)):
        result += int(num[i])
    return result
lst = []
for i in range(1, 10001):
    lst.append(d(i))
    
for i in range(1,10001):
    if i not in lst:
        print(i)
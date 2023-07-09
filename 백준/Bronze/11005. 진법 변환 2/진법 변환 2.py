## 11005
n, b = map(int, input().split())
result = []
while n > 0:
    if n%b >= 10:
        result.append(chr((n%b)+55))
    else:
        result.append(n%b)
    n //= b
result.reverse()
for i in range(len(result)):
    print(result[i], end='')
## 2745
n, b = input().split()
n = list(n)
b = int(b)
result = 0
for i in range(len(n)):
    if n[i].isalpha():
        n[i] = ord(n[i])-55
    else:
        n[i] = int(n[i])
for i in range(len(n)):
    result += n[i]*(b**(len(n)-1-i))
print(result)
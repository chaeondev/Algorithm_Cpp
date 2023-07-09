n = int(input())
def counter(n):
    if n == 0:
        return 2
    else:
        return counter(n-1) + 2**(n-1)
print(counter(n)**2)
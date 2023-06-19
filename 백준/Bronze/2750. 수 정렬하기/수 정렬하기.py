n = int(input())
listed = []
for i in range(n):
    listed.append(int(input()))
listed.sort()
for i in range(n):
    print(listed[i])
string = input()
count = 0
for i in range(len(string)-1):
    if string[i] != string[i+1]:
        count += 1

if count <= 1:
    print(count)
else:
    group = count + 1
    print(group//2)
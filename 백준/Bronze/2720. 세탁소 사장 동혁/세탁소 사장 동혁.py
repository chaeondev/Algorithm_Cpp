## 2720
t = int(input())
for _ in range(t):
    change = int(input())
    quarter = change // 25
    change = change % 25
    dime = change // 10
    change = change % 10
    nickel = change // 5
    change = change % 5
    penny = change
    print(quarter, dime, nickel, penny)
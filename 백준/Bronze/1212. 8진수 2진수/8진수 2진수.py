n = input()

# 8진수를 10진수로 변환
decimal = int(n, 8)

# 10진수를 2진수로 변환
binary = bin(decimal)[2:]

print(binary)
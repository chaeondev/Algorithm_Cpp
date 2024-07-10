import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }

var sum = 0

for i in input {
    sum += i * i
}

let result = sum % 10

print(result)

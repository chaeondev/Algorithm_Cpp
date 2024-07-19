
import Foundation

let n = Int(readLine()!)!
let numberArray = readLine()!.split(separator: " ").map { Int($0)! }

var count = 0
for number in numberArray {
    if isPrime(number) {
        count += 1
    }
}

print(count)

func isPrime(_ x: Int) -> Bool {
    let midNum = Int(sqrt(Double(x)))
    if midNum > 2 {
        for i in 2...midNum {
            if x % i == 0 {
                return false
            }
        }
    } else {
        if x == 1 {
            return false
        }

        if x == 2 {
            return true
        }

        for i in 2..<x {
            if x % i == 0 {
                return false
            }
        }
    }
    
    return true
}
import Foundation

let a = Int(readLine()!)!
let b = Int(readLine()!)!
let c = Int(readLine()!)!

let number = a + b - c
print(number)

let stringResult = String(a) + String(b)
let result = Int(stringResult)! - c
print(result)
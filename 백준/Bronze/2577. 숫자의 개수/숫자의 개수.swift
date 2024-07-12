import Foundation

let a = Int(readLine()!)!
let b = Int(readLine()!)!
let c = Int(readLine()!)!

let number = a * b * c

for i in 0...9 {
    let result = String(number).filter { $0 == Character("\(i)") }.count
    print(result)
}
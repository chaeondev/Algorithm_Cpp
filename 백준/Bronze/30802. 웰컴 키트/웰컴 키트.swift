import Foundation

let n = Int(readLine()!)!
let sizeArray = readLine()!.split(separator: " ").map { Int($0)! }
let (s, m, l, xl, xxl, xxxl) = (sizeArray[0], sizeArray[1], sizeArray[2], sizeArray[3], sizeArray[4], sizeArray[5])
let orderArray = readLine()!.split(separator: " ").map { Int($0)! }
let (t, p) = (orderArray[0], orderArray[1])

//result : T / P 1

var tCount = 0
for size in sizeArray {
    tCount += (size / t)
    if (size % t) != 0 {
        tCount += 1
    }
}

var pCount = n / p
var onePenCount = n % p

print(tCount)
print("\(pCount) \(onePenCount)")
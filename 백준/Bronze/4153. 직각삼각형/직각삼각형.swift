import Foundation

while let input = readLine(),
    input != "0 0 0" {
    let arrayInt = input.split(separator: " ").map { Int($0)! }
    let sortedArray = arrayInt.sorted(by: >)
    let (a, b, c) = (sortedArray[0], sortedArray[1], sortedArray[2])
    if a * a == (b * b) + (c * c) {
        print("right")
    } else {
        print("wrong")
    }
}
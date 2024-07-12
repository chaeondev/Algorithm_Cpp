import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }

let ascendingScale: [Int] = Array(1...8)
let descendingScale: [Int] = Array(1...8).reversed()

if input == ascendingScale {
    print("ascending")
} else if input == descendingScale {
    print("descending")
} else {
    print("mixed")
}
import Foundation

// MARK: - 19532

let array = readLine()!.split(separator: " ").map { Int(String($0))! }


for x in -999...999 {
    for y in -999...999 {
        if array[0] * x + array[1] * y == array[2] {
            if array[3] * x + array[4] * y == array[5] {
                print(x, y)
            }
        }
    }
}

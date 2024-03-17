let n = Int(readLine()!)!
var cnt = 0

for a in 0...n {
    for b in 0...n {
        for c in 0...n {
            if a > 0 && a % 2 == 0 && b > 0 && b + 2 <= c && c > 0 && a + b + c == n {
                cnt += 1
            }
        }
    }
}

print(cnt)

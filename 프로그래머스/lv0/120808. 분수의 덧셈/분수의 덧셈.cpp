#include <string>
#include <vector>

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;
    int n = numer1*denom2 + numer2*denom1;
    int dn = denom1*denom2;
    int gcd = 0;
    
    for(int i=2; i<=min(n,dn); i++) {
        if(n % i == 0 && dn % i ==0) {
            gcd = i;
        }
    }
    if(gcd != 0) {
        n /= gcd;
        dn /= gcd;
    }
    
    answer.push_back(n);
    answer.push_back(dn);
    
    return answer;
}



/*1번 시도*/

// #include <string>
// #include <vector>

// using namespace std;

// vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
//     vector<int> answer;
//     int n = numer1*denom2 + numer2*denom1;
//     int dn = denom1*denom2;
//     int gcd;
    
//     for(int i=2; i<=min(n,dn); i++) {
//         if(n % i == 0 && dn % i ==0) {
//             gcd = i;
//         }
//     }
//     if(gcd != 0) {
//         n /= gcd;
//         dn /= gcd;
//     }
    
//     answer.push_back(n);
//     answer.push_back(dn);
    
//     return answer;
// }

// 내가 잘못한 부분
// 1. gcd를 초기화 안하는 멍청한 실수를 저지름
// 2. 시간제약이 없어서 이런 방식을 선택했지만 시간 제약이 있을경우 for문을 i++가 아니라 i--로 바꾸면 훨씬 시간이 절약되면서 최대공약수를 구할 수 있을 것 같음

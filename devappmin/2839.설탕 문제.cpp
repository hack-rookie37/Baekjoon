/**
 * @file 2839.설탕 문제.cpp
 * @author @devappmin
 * @brief 설탕문제
 * @version 0.1
 * @date 2021-12-28
 *
 * @copyright Copyright @devappmin (c) 2021
 *
 */

#include <iostream>

using namespace std;

int solution() {
    int n;
    cin >> n;

    for (int f = 0; f <= n / 3; f++) {
        for (int t = 0; t <= n / 5; t++) {
            if (t * 5 + f * 3 == n)
                return f + t;
            else if (t * f > n)
                break;
        }
    }
    return -1;
}

int main() {
    cout << solution();
    return 0;
}
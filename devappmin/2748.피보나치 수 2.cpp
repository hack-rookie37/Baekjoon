/**
 * @file 2748.피보나치 수 2.cpp
 * @author @devappmin
 * @brief 피보나치 수 2(브론즈1)
 * @version 0.1
 * @date 2022-01-15
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>

#define MAX 90

using namespace std;

long long arr[MAX] = {0, 1};

void solution(int leng) {
    for (int i = 2; i <= leng; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
    }

    cout << arr[leng];
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int leng;
    cin >> leng;

    solution(leng);
    return 0;
}

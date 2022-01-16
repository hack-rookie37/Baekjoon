/**
 * @file 2156.포도주 시식.cpp
 * @author @devappmin
 * @brief 포도주 시식
 * @version 0.1
 * @date 2022-01-11
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <algorithm>
#include <iostream>

int arr[10001];
int dp[10001];

using namespace std;

int max(int a, int b, int c) {
    return (a > b) ? (c > a) ? c : a : (b > c) ? b
                                               : c;
}

void solution(int len) {
    dp[0] = arr[0];
    dp[1] = arr[0] + arr[1];

    for (int i = 2; i < len; i++) {
        dp[i] = max(dp[i - 1], dp[i - 3] + arr[i - 1] + arr[i], dp[i - 2] + arr[i]);
    }

    cout << dp[len - 1];
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int l, input;
    cin >> l;

    for (int idx = 0; idx < l; idx++) {
        cin >> input;
        arr[idx] = input;
    }

    solution(l);

    return 0;
}
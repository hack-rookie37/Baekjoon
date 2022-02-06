/**
 * @file 9095 1, 2, 3 더하기.cpp
 * @author @devappmin
 * @brief 1, 2, 3 더하기(실버3)
 * @version 0.1
 * @date 2022-02-01
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 12

using namespace std;

int dp[MAX] = {0, 1, 2, 4};

void solution() {
    for (int i = 4; i < MAX; i++) {
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
    }
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int t, n;
    cin >> t;

    solution();
    for (int i = 0; i < t; i++) {
        cin >> n;
        cout << dp[n] << "\n";
    }

    return 0;
}

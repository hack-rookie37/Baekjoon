/**
 * @file 11047.동전 0.cpp
 * @author @devappmin
 * @brief 동전 0 (실버2)
 * @version 0.1
 * @date 2022-01-21
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

vector<int> coins;

void solution(int n, int k) {
    int ans = 0;
    for (int i = coins.size() - 1; i >= 0; i--) {
        ans += k / coins[i];
        k %= coins[i];
    }
    cout << ans;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    cout.sync_with_stdio(0);

    int n, k, input;
    cin >> n >> k;

    for (int i = 0; i < n; i++) {
        cin >> input;
        coins.push_back(input);
    }

    solution(n, k);

    return 0;
}
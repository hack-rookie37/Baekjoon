/**
 * @file 1931.회의실 배정.cpp
 * @author @devappmin
 * @brief 회의실 배정(실버2)
 * @version 0.1
 * @date 2022-01-25
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

vector<pair<int, int>> v;

void solution(int n) {
    int ans = 0;
    int cur = 0;

    for (int i = 0; i < n; i++) {
        if (cur <= v[i].second) {
            cur = v[i].first;
            ans++;
        }
    }

    cout << ans;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int n, st, et;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> st >> et;
        v.push_back({et, st});
    }

    sort(v.begin(), v.end());

    solution(n);

    return 0;
}
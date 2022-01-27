/**
 * @file 1107.리모컨.cpp
 * @author @devappmin
 * @brief 리모컨(골드5)
 * @version 0.1
 * @date 2022-01-27
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 1000000

using namespace std;

bool canJump(int dest, vector<int> broken) {
    for (int i : broken) {
        for (int j : to_string(dest)) {
            if (i == j - '0')
                return false;
        }
    }
    return true;
}

void solution(int n, int m, vector<int> broken) {
    int cursor = 100;
    int ans = abs(n - cursor);

    for (int i = 0; i <= MAX; i++) {
        if (canJump(i, broken)) {
            int temp = abs(n - i) + to_string(i).length();
            ans = min(ans, temp);
        }
    }

    cout << ans;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int n, m;
    cin >> n >> m;

    vector<int> broken(m);

    for (int i = 0; i < m; i++) {
        cin >> broken[i];
    }

    solution(n, m, broken);

    return 0;
}
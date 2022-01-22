/**
 * @file 11399.ATM.cpp
 * @author @devappmin
 * @brief ATM (실버3)
 * @version 0.1
 * @date 2022-01-22
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 1005

using namespace std;

int p[MAX];

void solution(int n) {
    sort(&p[1], &p[n + 1]);

    int ans = 0;
    for (int i = n; i > 0; i--) {
        ans += p[n - i + 1] * i;
    }

    cout << ans;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    cout.sync_with_stdio(0);

    int n;
    cin >> n;

    for (int i = 1; i <= n; i++) {
        cin >> p[i];
    }

    solution(n);

    return 0;
}
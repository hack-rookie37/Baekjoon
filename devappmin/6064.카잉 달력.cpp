/**
 * @file 6064.카잉 달력.cpp
 * @author @devappmin
 * @brief 카잉 달력(실버1)
 * @version 0.1
 * @date 2022-02-03
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

void solution(int m, int n, int x, int y) {
    bool ans = false;

    while (x <= m * n) {
        if ((x - y) % n == 0) {
            ans = true;
            break;
        }
        x += m;
    }
    cout << (ans ? x : -1) << "\n";
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int loop;
    cin >> loop;

    for (int i = 0; i < loop; i++) {
        int m, n, x, y;
        cin >> m >> n >> x >> y;
        solution(m, n, x, y);
    }
    return 0;
}
/**
 * @file 2630.색종이 만들기.cpp
 * @author @devappmin
 * @brief 색종이 만들기(실버3)
 * @version 0.1
 * @date 2022-01-26
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 129

using namespace std;

int paper[MAX][MAX];

int ans[2] = {0, 0};

void p(int y, int x, int size) {
    int v = paper[y][x];

    for (int i = y; i < y + size; i++) {
        for (int j = x; j < x + size; j++) {
            if (paper[i][j] != v) {
                p(y, x, size / 2);
                p(y, x + size / 2, size / 2);
                p(y + size / 2, x, size / 2);
                p(y + size / 2, x + size / 2, size / 2);
                return;
            }
        }
    }

    ans[v]++;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> paper[i][j];
        }
    }

    p(0, 0, n);

    cout << ans[0] << "\n"
         << ans[1];

    return 0;
}
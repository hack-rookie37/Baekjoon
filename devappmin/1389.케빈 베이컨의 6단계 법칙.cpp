/**
 * @file 1389.케빈 베이컨의 6단계 법칙.cpp
 * @author @devappmin
 * @brief 케빈 베이컨의 6단계 법칙 (실버1)
 * @version 0.1
 * @date 2022-01-24
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define INF 999999999

#define MAX 105

using namespace std;

int w[MAX][MAX];

void solution(int n) {
    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (w[i][k] + w[k][j] < w[i][j])
                    w[i][j] = w[i][k] + w[k][j];
            }
        }
    }

    int ans = 0, best = INF;
    for (int i = 1; i <= n; i++) {
        int val = 0;
        for (int j = 1; j <= n; j++) {
            if (w[i][j] != INF && i != j)
                val += w[i][j];
        }
        if (val < best)
            best = val, ans = i;
    }
    cout << ans;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int n, m;

    cin >> n >> m;

    fill(&w[0][0], &w[n][n], INF);

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        w[a][b] = 1;
        w[b][a] = 1;
    }

    solution(n);

    return 0;
}
/**
 * @file 11404.플로이드.cpp
 * @author @devappmin
 * @brief 플로이드 (골드4)
 * @version 0.1
 * @date 2022-01-22
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 105
#define NIL 99999999

using namespace std;

int w[MAX][MAX];
int d[MAX][MAX];

void solution(int n) {
    copy(&w[0][0], &w[n + 1][n + 1], &d[0][0]);

    for (int k = 1; k <= n; k++) {
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (d[i][k] + d[k][j] < d[i][j]) {
                    d[i][j] = d[i][k] + d[k][j];
                }
            }
        }
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cout << (d[i][j] == NIL ? 0 : d[i][j]) << " ";
        }
        cout << "\n";
    }
}

int main() {
    cin.tie(0);
    cout.tie(0);
    cout.sync_with_stdio(0);

    int n, m;
    int a, b, c;
    cin >> n >> m;

    fill(&w[0][0], &w[n + 1][n + 1], NIL);

    for (int i = 0; i <= n; i++) {
        w[i][i] = 0;
    }

    for (int i = 0; i < m; i++) {
        cin >> a >> b >> c;
        if (w[a][b] > c)
            w[a][b] = c;
    }
    solution(n);

    return 0;
}
/**
 * @file 14502.연구소.cpp
 * @author @devappmin
 * @brief 연구소(골드5)
 * @version 0.1
 * @date 2022-01-15
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 12

using namespace std;

vector<vector<int>> world(MAX, vector<int>(MAX, 1));

vector<pair<int, int>> v;

vector<pair<int, int>> virus;

int li[2][4] = {{1, -1, 0, 0}, {0, 0, 1, -1}};

int solution(int n, int m, int remain, vector<vector<int>> w, int va, int vb, int vc) {
    w[v[va].first][v[va].second] = 1;
    w[v[vb].first][v[vb].second] = 1;
    w[v[vc].first][v[vc].second] = 1;

    queue<pair<int, int>> q;

    for (int i = 0; i < virus.size(); i++) {
        q.push(virus[i]);
    }

    while (!q.empty()) {
        int y, x;
        tie(y, x) = q.front();
        q.pop();

        for (int i = 0; i < 4; i++) {
            if (w[y + li[0][i]][x + li[1][i]] == 0) {
                w[y + li[0][i]][x + li[1][i]] = w[y][x] + 1;
                q.push(pair<int, int>(y + li[0][i], x + li[1][i]));
                remain--;
            }
        }
    }

    return remain - 3;
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int n, m, input, remain = 0;

    cin >> n >> m;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            cin >> world[i][j];

            if (world[i][j] == 0) {
                v.push_back(pair<int, int>(i, j));
                remain++;
            } else if (world[i][j] == 2) {
                virus.push_back(pair<int, int>(i, j));
            }
        }
    }

    int temp = remain;
    int ans = 0;

    for (int j = 0; j < v.size() - 2; j++) {
        for (int k = 1; k < v.size() - 1; k++) {
            for (int l = 2; l < v.size(); l++) {
                if (l == k || l == j || j == k)
                    continue;

                temp = solution(n, m, remain, world, j, k, l);

                if (temp > ans) {
                    ans = temp;
                }
            }
        }
    }

    cout << ans;

    return 0;
}
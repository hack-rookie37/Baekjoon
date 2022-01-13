/**
 * @file 1012.유기농 배추.cpp
 * @author @devappmin
 * @brief 유기농 배추(실버2)
 * @version 0.1
 * @date 2022-01-13
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 55

using namespace std;

int li[2][4] = {{1, -1, 0, 0}, {0, 0, 1, -1}};

void solution() {
    int world[MAX][MAX];

    queue<pair<int, int> > q;
    queue<pair<int, int> > q2;
    int m, n, k;
    int ans = 0;

    cin >> m >> n >> k;

    fill(&world[0][0], &world[m + 2][n + 2], 0);

    for (int i = 0; i < k; i++) {
        int x, y;
        cin >> x >> y;
        world[y + 1][x + 1] = 1;
        q.push(pair<int, int>(y + 1, x + 1));
    }

    while (!q.empty()) {
        if (q2.empty()) {
            q2.push(q.front());
            q.pop();
        }

        int y, x;
        tie(y, x) = q2.front();
        q2.pop();

        if (world[y][x] == 1)
            ans++;

        for (int i = 0; i < 4; i++) {
            if (world[y + li[0][i]][x + li[1][i]] == 1) {
                world[y + li[0][i]][x + li[1][i]] = world[y][x] + 1;
                q2.push(pair<int, int>(y + li[0][i], x + li[1][i]));
            }
        }
    }

    cout << ans << "\n";
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int loop;

    cin >> loop;

    for (int i = 0; i < loop; i++) {
        solution();
    }

    return 0;
}
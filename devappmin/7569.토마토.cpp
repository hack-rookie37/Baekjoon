/**
 * @file 7569.토마토.cpp
 * @author @devappmin
 * @brief 토마토(실버1)
 * @version 0.1
 * @date 2022-01-13
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

// 7576 토마토의 3차원버전

#include <bits/stdc++.h>

#include <iostream>

#define MAX 105

using namespace std;

int world[MAX][MAX][MAX];

int remain = 0, day = 1;

queue<tuple<int, int, int> > q;

int li[3][6] = {{1, -1, 0, 0, 0, 0}, {0, 0, 1, -1, 0, 0}, {0, 0, 0, 0, 1, -1}};

void colonize(int x, int y, int z) {
    for (int i = 0; i < 6; i++) {
        if (world[z + li[0][i]][y + li[1][i]][x + li[2][i]] == 0) {
            world[z + li[0][i]][y + li[1][i]][x + li[2][i]] = world[z][y][x] + 1;
            q.push(tuple<int, int, int>(z + li[0][i], y + li[1][i], x + li[2][i]));
            remain--;

            if (world[z + li[0][i]][y + li[1][i]][x + li[2][i]] > day)
                day = world[z + li[0][i]][y + li[1][i]][x + li[2][i]];
        }
    }
}

void solution(int x, int y, int z) {
    while (!q.empty()) {
        int h, c, r;
        tie(h, c, r) = q.front();
        q.pop();

        colonize(r, c, h);
    }

    if (remain != 0)
        cout << "-1";
    else
        cout << day - 1;
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int m, n, h;

    cin >> m >> n >> h;

    fill(&world[0][0][0], &world[h + 2][n + 2][m + 2], -1);

    for (int i = 1; i <= h; i++) {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= m; k++) {
                cin >> world[i][j][k];

                if (world[i][j][k] == 1)
                    q.push(tuple<int, int, int>(i, j, k));
                else if (world[i][j][k] == 0)
                    remain++;
            }
        }
    }

    solution(m, n, h);

    return 0;
}
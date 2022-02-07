/**
 * @file 16234.인구 이동.cpp
 * @author @devappmin
 * @brief 인구 이동(골드5)
 * @version 0.1
 * @date 2022-02-06
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 51

using namespace std;

int world[MAX][MAX];
int visited[MAX][MAX];

int li[2][4] = {{1, -1, 0, 0}, {0, 0, 1, -1}};

queue<pair<int, int> > q;
queue<pair<int, int> > qq;
void colonize(int y, int x, int n, int l, int r) {
    for (int i = 0; i < 4; i++) {
        int dy = y + li[0][i];
        int dx = x + li[1][i];

        if (dy == 0 || dx == 0 || dy == n + 1 || dx == n + 1)
            continue;

        if (visited[dy][dx])
            continue;

        int dv = abs(world[y][x] - world[dy][dx]);

        if (dv >= l && dv <= r) {
            visited[dy][dx] = visited[y][x];
            qq.push({dy, dx});
        }
    }
}

bool solution(int n, int l, int r) {
    bool finished = true;

    int c = 1;

    while (!q.empty()) {
        if (qq.empty()) {
            int ty, tx;
            tie(ty, tx) = q.front();
            if (!visited[ty][tx]) {
                visited[ty][tx] = c++;
                qq.push({ty, tx});
                q.pop();
            } else {
                q.pop();
                continue;
            }
        }

        int y, x;
        tie(y, x) = qq.front();
        qq.pop();

        colonize(y, x, n, l, r);
    }

    int avg[c];
    int siz[c];
    memset(avg, 0, sizeof(avg));
    memset(siz, 0, sizeof(avg));
    for (int a = 1; a <= n; a++) {
        for (int b = 1; b <= n; b++) {
            avg[visited[a][b]] += world[a][b];
            siz[visited[a][b]]++;
        }
    }

    for (int a = 1; a <= n; a++) {
        for (int b = 1; b <= n; b++) {
            if (world[a][b] != (avg[visited[a][b] / siz[visited[a][b]]]))
                finished = false;

            world[a][b] = avg[visited[a][b]] / siz[visited[a][b]];
        }
    }

    return finished;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    memset(world, -1, sizeof(world));
    memset(visited, 0, sizeof(visited));

    int n, l, r;

    cin >> n >> l >> r;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> world[i][j];
            q.push({i, j});
        }
    }

    int ans = 0;
    queue<pair<int, int> > q2 = q;

    while (!solution(n, l, r)) {
        memset(visited, 0, sizeof(visited));
        q = q2;
        qq = queue<pair<int, int> >();
        ans++;
    }

    cout << ans;
    return 0;
}

// 10 15 20
// 20 30 25
// 40 22 10

// 20 20 20
// 20 20 20
// 40 20 10

// 20 20 20
// 20 20 16
// 40 16 16
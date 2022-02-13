/**
 * @file 16236.아기 상어.cpp
 * @author @devappmin
 * @brief 아기 상어(골드4)
 * @version 0.1
 * @date 2022-02-09
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

#define MAX 22

int world[MAX][MAX];
int visited[MAX][MAX];
int n;
int lvl = 2;
int sexp = 0;
int mv = 0;

int by[4] = {-1, 0, 0, 1};
int bx[4] = {0, -1, 1, 0};

queue<pair<int, int> > sharkq;
priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > eatPos;

bool colonize(int y, int x) {
    for (int i = 0; i < 4; i++) {
        int dy = y + by[i];
        int dx = x + bx[i];

        if (dy < 0 || dy >= n || dx < 0 || dx >= n)
            continue;

        if (visited[dy][dx] || world[dy][dx] > lvl)
            continue;

        if (world[dy][dx] < lvl && world[dy][dx] != 0) {
            if (eatPos.size() == 0)
                eatPos.push({dy, dx});
            else if (visited[eatPos.top().first][eatPos.top().second] == visited[y][x] + 1) {
                eatPos.push({dy, dx});
            }

            visited[dy][dx] = visited[y][x] + 1;
            sharkq.push({dy, dx});
            return true;
        }

        visited[dy][dx] = visited[y][x] + 1;
        sharkq.push({dy, dx});
    }

    return false;
}

bool solution() {
    int val = 5000;
    while (!sharkq.empty()) {
        int y, x;
        tie(y, x) = sharkq.front();
        sharkq.pop();

        if (visited[y][x] > val)
            break;

        if (colonize(y, x)) {
            if (eatPos.size() == 1)
                val = visited[eatPos.top().first][eatPos.top().second];
        }
    }

    if (eatPos.size() > 0) {
        sharkq = queue<pair<int, int> >();
        sharkq.push(eatPos.top());
        mv = visited[eatPos.top().first][eatPos.top().second];
        world[eatPos.top().first][eatPos.top().second] = 0;
        sexp++;
        if (sexp == lvl) {
            lvl++;
            sexp = 0;
        }
        return true;
    } else {
        return false;
    }
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    cin >> n;

    int remain = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> world[i][j];

            if (world[i][j] == 0)
                continue;

            if (world[i][j] == 9) {
                sharkq.push({i, j});
                visited[i][j] = 1;
                world[i][j] = 0;
            } else
                remain++;
        }
    }

    while (solution() && remain) {
        memset(visited, 0, sizeof(visited));
        visited[eatPos.top().first][eatPos.top().second] = mv;
        eatPos = priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > >();
        remain--;
    }

    cout << (mv > 0 ? mv - 1 : 0);

    return 0;
}
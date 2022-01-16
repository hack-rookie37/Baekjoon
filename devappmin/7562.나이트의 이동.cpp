/**
 * @file 7562.나이트의 이동.cpp
 * @author @devappmin
 * @brief 나이트의 이동(실버2)
 * @version 0.1
 * @date 2022-01-12
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

int li[2][8] = {{-2, -1, 1, 2, -2, -1, 1, 2}, {1, 2, 2, 1, -1, -2, -2, -1}};

void solution(int size, int sy, int sx, int dy, int dx) {
    int map[size + 1][size + 1];

    fill(&map[0][0], &map[size][size], 0);

    queue<pair<int, int> > q;
    q.push(pair<int, int>(sy, sx));

    while (!q.empty()) {
        pair<int, int> pos = q.front();
        q.pop();

        if (sy == dy && sx == dx) break;

        for (int i = 0; i < 8; i++) {
            if (pos.first + li[0][i] >= 0 && pos.first + li[0][i] < size &&
                pos.second + li[1][i] >= 0 && pos.second + li[1][i] < size) {
                if (map[pos.first + li[0][i]][pos.second + li[1][i]] == 0) {
                    map[pos.first + li[0][i]][pos.second + li[1][i]] = map[pos.first][pos.second] + 1;
                    q.push(pair<int, int>(pos.first + li[0][i], pos.second + li[1][i]));
                }
            }
        }
    }

    cout << map[dy][dx] << "\n";
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int loop;
    cin >> loop;

    for (int i = 0; i < loop; i++) {
        int size, sy, sx, dy, dx;
        cin >> size >> sy >> sx >> dy >> dx;

        solution(size, sy, sx, dy, dx);
    }

    return 0;
}
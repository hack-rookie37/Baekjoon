/**
 * @file 4963.섬의 개수.cpp
 * @author @devappmin
 * @brief 섬의 개수(실버2)
 * @version 0.1
 * @date 2022-01-19
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 * 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
 * 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
 * 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.
 *
 * 입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
 * 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
 * 입력의 마지막 줄에는 0이 두 개 주어진다.
 *
 * 각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

int li[2][8] = {{1, -1, 0, 0, 1, 1, -1, -1}, {0, 0, 1, -1, 1, -1, 1, -1}};

void solution(int w, int h) {
    int world[h + 3][w + 3];
    int ans = 0;
    queue<pair<int, int> > q;
    queue<pair<int, int> > qq;

    fill(&world[0][0], &world[h + 2][w + 2], 0);

    for (int i = 1; i <= h; i++) {
        for (int j = 1; j <= w; j++) {
            cin >> world[i][j];
            if (world[i][j] == 1)
                q.push(pair<int, int>(i, j));
        }
    }

    while (!q.empty()) {
        if (qq.empty()) {
            pair<int, int> p = q.front();

            q.pop();

            if (world[p.first][p.second] == 1) {
                qq.push(p);
                ans++;
            } else
                continue;
        }

        int y, x;
        tie(y, x) = qq.front();
        qq.pop();

        for (int i = 0; i < 8; i++) {
            if (world[y + li[0][i]][x + li[1][i]] == 1) {
                world[y + li[0][i]][x + li[1][i]] = world[y][x] + 1;
                qq.push(pair<int, int>(y + li[0][i], x + li[1][i]));
            }
        }
    }

    cout << ans << "\n";
}

int main() {
    cin.tie(0);
    cout.tie(0);
    cout.sync_with_stdio(0);

    int w, h;
    cin >> w >> h;

    while (w != 0 && h != 0) {
        solution(w, h);
        cin >> w >> h;
    }

    return 0;
}
/**
 * @file 2206.벽 부수고 이동하기.cpp
 * @author @devappmin
 * @brief 벽 부수고 이동하기 (골드 4)
 * @version 0.1
 * @date 2022-01-12
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <tuple>

#define MAX 1002

using namespace std;

queue<tuple<int, int, int> > q;

int li[2][4] = {{1, -1, 0, 0}, {0, 0, 1, -1}};

int map[MAX][MAX][2];

void colonize(int y, int x, int broken, int n, int m) {
    if (x >= 1 && x <= m && y >= 1 && y <= n) {
        for (int i = 0; i < 4; i++) {
            if (map[y + li[0][i]][x + li[1][i]][broken] == -1 && broken == 0) {
                map[y + li[0][i]][x + li[1][i]][1] = map[y][x][0] + 1;
                q.push(tuple<int, int, int>(y + li[0][i], x + li[1][i], 1));
            } else if (map[y + li[0][i]][x + li[1][i]][broken] == 0) {
                map[y + li[0][i]][x + li[1][i]][broken] = map[y][x][broken] + 1;
                q.push(tuple<int, int, int>(y + li[0][i], x + li[1][i], broken));
            }
        }
    }
}

void solution(int n, int m) {
    q.push(tuple<int, int, int>(1, 1, 0));

    while (!q.empty()) {
        int y, x, broken;
        tie(y, x, broken) = q.front();

        if (x == m && y == n) {
            cout << map[y][x][broken] + 1;
            return;
        }
        q.pop();
        colonize(y, x, broken, n, m);
    }

    if (map[n][m][1] == 0)
        cout << -1;
    else
        cout << map[n][m][1] + 1;
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int n, m;
    cin >> n >> m;

    fill(&map[0][0][0], &map[n + 1][m + 1][1] + 1, -1);

    for (int i = 1; i <= n; i++) {
        string str;
        cin >> str;
        for (int j = 1; j <= m; j++) {
            if (str[j - 1] == '1')
                str[j - 1] = '0' - 1;

            map[i][j][0] = str[j - 1] - '0';
            map[i][j][1] = str[j - 1] - '0';
        }
    }

    solution(n, m);

    return 0;
}
/**
 * @file 4179.불.cpp
 * @author @devappmin
 * @brief 불
 * @version 0.1
 * @date 2022-01-01
 *
 * @copyright Copyright (c) 2021 @devappmin
 *
 */

#include <iostream>
#include <queue>
#include <utility>

#define MAX 1002

using namespace std;

int fMap[MAX][MAX];
int pMap[MAX][MAX];
int ans = -1;
queue<pair<int, int> > fq;
queue<pair<int, int> > pq;

int pos[2][4] = {{1, -1, 0, 0}, {0, 0, 1, -1}};

void spreadFire(int x, int y) {
    for (int i = 0; i < 4; i++) {
        if (fMap[y + pos[1][i]][x + pos[0][i]] == 0) {
            fMap[y + pos[1][i]][x + pos[0][i]] = fMap[y][x] + 1;
            fq.push(pair<int, int>(y + pos[1][i], x + pos[0][i]));
        }
    }
}

void movement(int x, int y) {
    for (int i = 0; i < 4; i++) {
        if (pMap[y + pos[1][i]][x + pos[0][i]] == 0 && (pMap[y + pos[1][i]][x + pos[0][i]] < fMap[y + pos[1][i]][x + pos[0][i]] || fMap[y + pos[1][i]][x + pos[0][i]] == 0)) {
            pMap[y + pos[1][i]][x + pos[0][i]] = pMap[y][x] + 1;
            pq.push(pair<int, int>(y + pos[1][i], x + pos[0][i]));
        } else if (pMap[y + pos[1][i]][x + pos[0][i]] == -2 && (pMap[y][x] < fMap[y][x] || fMap[y][x] == 0)) {
            ans = pMap[y][x];
            return;
        }
    }
}

void solution() {
    while (!fq.empty()) {
        int x = fq.front().second;
        int y = fq.front().first;
        fq.pop();
        spreadFire(x, y);
    }

    while (!pq.empty()) {
        int x = pq.front().second;
        int y = pq.front().first;
        pq.pop();
        movement(x, y);

        if (ans != -1)
            break;
    }
}

int main() {
    cout.sync_with_stdio(0);
    cin.tie(0);

    int r, c, i, j;
    char val;

    cin >> r >> c;

    for (i = 0; i <= r + 1; i++) {
        for (j = 0; j <= c + 1; j++) {
            if (i == 0 || i == r + 1 || j == 0 || j == c + 1) {
                fMap[i][j] = -2;
                pMap[i][j] = -2;
            } else {
                cin >> val;

                if (val == '#') {
                    fMap[i][j] = -1;
                    pMap[i][j] = -1;
                } else if (val == '.') {
                    fMap[i][j] = 0;
                    pMap[i][j] = 0;
                } else if (val == 'J') {
                    fMap[i][j] = 0;
                    pMap[i][j] = 1;
                    pq.push(pair<int, int>(i, j));
                } else if (val == 'F') {
                    pMap[i][j] = 0;
                    fMap[i][j] = 1;
                    fq.push(pair<int, int>(i, j));
                }
            }
        }
    }

    solution();

    ans <= 0 ? cout << "IMPOSSIBLE" : cout << ans;
    return 0;
}
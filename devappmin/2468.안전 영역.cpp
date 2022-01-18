/**
 * @file 2468.안전 영역.cpp
 * @author @devappmin
 * @brief 안전 영역(실버1)
 * @version 0.1
 * @date 2022-01-17
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 105
#define VISITED 200

using namespace std;

vector<vector<int> > w(MAX, vector<int>(MAX, VISITED));
int li[2][4] = {{1, -1, 0, 0}, {0, 0, 1, -1}};

int solution(vector<vector<int> > world, int size, int lv, queue<pair<int, int> > q) {
    queue<pair<int, int> > q2;
    int ans = 0;

    while (!q.empty()) {
        if (q2.empty()) {
            pair<int, int> c = q.front();
            q.pop();

            if (world[c.first][c.second] <= lv)
                continue;

            if (world[c.first][c.second] != VISITED) {
                world[c.first][c.second] = VISITED;
                ans++;
            }
            q2.push(c);
        }

        int y, x;
        tie(y, x) = q2.front();
        q2.pop();

        for (int i = 0; i < 4; i++) {
            if (world[y + li[0][i]][x + li[1][i]] > lv && world[y + li[0][i]][x + li[1][i]] != VISITED) {
                world[y + li[0][i]][x + li[1][i]] = VISITED;
                q2.push(pair<int, int>(y + li[0][i], x + li[1][i]));
            }
        }
    }
    return ans;
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    queue<pair<int, int> > q;

    int size, maxlv = 0, ans = 0, temp;
    cin >> size;

    for (int i = 1; i <= size; i++) {
        for (int j = 1; j <= size; j++) {
            cin >> w[i][j];
            q.push(pair<int, int>(i, j));
            if (w[i][j] > maxlv)
                maxlv = w[i][j];
        }
    }
    for (int i = 0; i < maxlv; i++) {
        temp = solution(w, size, i, q);
        if (temp > ans)
            ans = temp;
    }

    cout << ans;

    return 0;
}
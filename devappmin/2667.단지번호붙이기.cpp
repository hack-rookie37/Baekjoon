/**
 * @file 2667.단지번호붙이기.cpp
 * @author @devappmin
 * @brief 단지번호붙이기
 * @version 0.1
 * @date 2022-01-04
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <utility>

#define MAX 27

using namespace std;

int matrix[MAX][MAX];

queue<pair<int, int> > q;
queue<pair<int, int> > q2;
int ans[MAX * MAX];

int li[2][4] = {{1, -1, 0, 0}, {0, 0, 1, -1}};

void colonize(pair<int, int> p, int val) {
    for (int i = 0; i < 4; i++) {
        if (matrix[p.first + li[0][i]][p.second + li[1][i]] == 1) {
            matrix[p.first + li[0][i]][p.second + li[1][i]] = val;
            q2.push(pair<int, int>(p.first + li[0][i], p.second + li[1][i]));
        }
    }
}

void solution(int size) {
    int val = 1;
    while (!q.empty()) {
        if (q2.empty()) {
            pair<int, int> c = q.front();
            q.pop();

            if (matrix[c.first][c.second] != 1)
                continue;

            matrix[c.first][c.second] = val + 1;
            ans[val - 1] = 0;
            q2.push(c);
            val++;
        }

        pair<int, int> pp = q2.front();
        q2.pop();
        ans[val - 2]++;
        colonize(pp, val);
    }

    sort(ans, ans + val - 1);
    cout << val - 1 << endl;
    for (int i = 0; i < val - 1; i++) {
        cout << ans[i] << endl;
    }
}

int main() {
    cout.sync_with_stdio(0);
    cin.tie(0);

    int size, i, j;
    string sinput;
    cin >> size;

    for (i = 0; i <= size + 1; i++) {
        if (i != 0 && i != size + 1)
            cin >> sinput;

        for (j = 0; j <= size + 1; j++) {
            if (i == 0 || i == size + 1 || j == 0 || j == size + 1) {
                matrix[i][j] = 0;
            } else {
                matrix[i][j] = sinput[j - 1] - '0';
                if (sinput[j - 1] == '1') {
                    q.push(pair<int, int>(i, j));
                }
            }
        }
    }
    solution(size);
    return 0;
}
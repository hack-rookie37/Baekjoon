/**
 * @file 7576.토마토.cpp
 * @author @devappmin
 * @brief 토마토
 * @version 0.1
 * @date 2021-12-30
 *
 * @copyright Copyright (c) 2021 @devappmin
 *
 */

#include <iostream>
#include <queue>
#include <utility>
#include <vector>

#define MAX 2001

using namespace std;

int box[MAX][MAX];
int ans = 0, remain = 0;

queue<pair<int, int> > q;

void colonizeBox(pair<int, int> p, int c, int r) {
    if (box[p.first + c][p.second + r] == 0) {
        box[p.first + c][p.second + r] = box[p.first][p.second] + 1;
        ans = box[p.first][p.second] + 1;
        q.push(pair<int, int>(p.first + c, p.second + r));
        remain--;
    }
}

// 이 부분 약간 무지성으로 짜서 마음에 안 듦..
void colonize(pair<int, int> p) {
    colonizeBox(p, 1, 0);
    colonizeBox(p, -1, 0);
    colonizeBox(p, 0, 1);
    colonizeBox(p, 0, -1);
}

void solution() {
    pair<int, int> c;
    while (!q.empty()) {
        c = q.front();
        q.pop();

        colonize(c);
    }
}

int main() {
    int n, m, num;

    scanf("%d %d", &n, &m);
    for (int i = 0; i <= m + 1; i++) {
        for (int j = 0; j <= n + 1; j++) {
            if (i == 0 || i == m + 1 || j == 0 || j == n + 1)
                box[i][j] = -1;
            else {
                scanf("%d", &num);
                box[i][j] = num;
                if (num == 1)
                    q.push(pair<int, int>(i, j));
                else if (num == 0)
                    remain++;
            }
        }
    }
    solution();

    if (ans == 0) ans++;

    printf("%d", remain <= 0 ? ans - 1 : -1);
    return 0;
}
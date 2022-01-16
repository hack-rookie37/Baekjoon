/**
 * @file 2178.미로 탐색.cpp
 * @author @devappmin
 * @brief 미로 탐색
 * @version 0.1
 * @date 2022-01-06
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>
#include <queue>
#include <utility>

#define MAX 102

using namespace std;

int arr[MAX][MAX];

int li[2][4] = {{1, -1, 0, 0}, {0, 0, 1, -1}};

queue<pair<int, int> > q;

void colonize(int n, int m) {
    for (int i = 0; i < 4; i++) {
        if (arr[n + li[0][i]][m + li[1][i]] == 1) {
            arr[n + li[0][i]][m + li[1][i]] = arr[n][m] + 1;
            q.push(pair<int, int>(n + li[0][i], m + li[1][i]));
        }
    }
}

void solution(int n, int m) {
    q.push(pair<int, int>(1, 1));

    while (!q.empty()) {
        pair<int, int> p = q.front();
        q.pop();

        colonize(p.first, p.second);
    }

    cout << arr[n][m];
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int n, m;
    string s;
    cin >> n >> m;

    fill(&arr[0][0], &arr[n + 1][m + 1] + 1, -1);

    for (int i = 1; i <= n; i++) {
        cin >> s;
        for (int j = 1; j <= m; j++)
            arr[i][j] = s[j - 1] - '0';
    }

    solution(n, m);

    return 0;
}
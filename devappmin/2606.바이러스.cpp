/**
 * @file 2606.바이러스.cpp
 * @author @devappmin
 * @brief 바이러스
 * @version 0.1
 * @date 2022-01-12
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>
#include <queue>
#include <vector>

#define MAX 101

using namespace std;

vector<int> v[MAX];

int visited[MAX];

queue<int> q;

void solution(int n, int m) {
    int ans = 0;
    visited[1] = true;
    q.push(1);

    while (!q.empty()) {
        int fr = q.front();

        q.pop();

        for (int i = 0; i < v[fr].size(); i++) {
            if (visited[v[fr][i]] == false) {
                visited[v[fr][i]] = true;
                q.push(v[fr][i]);
                ans++;
            }
        }
    }

    cout << ans;
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int n, m;

    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    fill(&visited[0], &visited[n] + 1, false);

    solution(n, m);

    return 0;
}
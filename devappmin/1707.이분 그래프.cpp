/**
 * @file 1707.이분 그래프.cpp
 * @author @devappmin
 * @brief 이분 그래프
 * @version 0.1
 * @date 2022-01-12
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>
#include <queue>
#include <vector>

using namespace std;

void solution(int v, int e) {
    vector<int> vt[v + 1];
    queue<int> q;

    char map[v + 1];
    bool visited[v + 1];

    bool ans = true;

    fill(&map[0], &map[v + 1] + 1, '0');
    fill(&visited[0], &visited[v + 1] + 1, false);

    for (int i = 0; i < e; i++) {
        int first, second;
        cin >> first >> second;

        vt[first].push_back(second);
        vt[second].push_back(first);
    }

    for (int vtx = 1; vtx <= v; vtx++) {
        if (map[vtx] == '0') {
            q.push(vtx);
            map[1] = '1';
        } else {
            continue;
        }

        while (!q.empty()) {
            int top = q.front();
            q.pop();

            if (map[top] == '0') {
                map[top] = '1';
            }

            if (map[top] == '1') {
                for (int i = 0; i < vt[top].size(); i++) {
                    if (map[vt[top][i]] == '1') {
                        ans = false;
                        break;
                    } else if (map[vt[top][i]] == '2') {
                        continue;
                    }
                    q.push(vt[top][i]);
                    map[vt[top][i]] = '2';
                }
            } else if (map[top] == '2') {
                for (int i = 0; i < vt[top].size(); i++) {
                    if (map[vt[top][i]] == '2') {
                        ans = false;
                        break;
                    } else if (map[vt[top][i]] == '1') {
                        continue;
                    }
                    q.push(vt[top][i]);
                    map[vt[top][i]] = '1';
                }
            }
        }
    }

    if (ans)
        cout << "YES\n";
    else
        cout << "NO\n";
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int loop;
    cin >> loop;

    for (int i = 0; i < loop; i++) {
        int v, e;
        cin >> v >> e;
        solution(v, e);
    }

    return 0;
}
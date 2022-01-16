/**
 * @file 13023.ABCDE.cpp
 * @author @devappmin
 * @brief ABCDE
 * @version 0.1
 * @date 2021-12-29
 *
 * @copyright Copyright (c) 2021 @devappmin
 *
 */

// 난독이어서 그런지 모든 노드를 전부 한 줄로 이어주는 것을 찾아야 하는 것으로 착각함.
// 최대한 recursion을 사용하지 않고 해결하려고 했으나 그냥 써버림..
// vim으로 코딩하고 싶어서 최대한 vim 명령어를 사용해서 코딩하는 쪽으로 진행

#include <iostream>
#include <vector>

#define MAX 2001
#define SOL 4

using namespace std;

bool ans = false;
bool visited[MAX] = {false};
vector<int> v[MAX];

void solution(int index, int n) {
    visited[index] = true;

    if (n == SOL) {
        ans = true;
        return;
    }

    for (int i = 0; i < v[index].size(); i++) {
        if (!visited[v[index][i]]) {
            solution(v[index][i], n + 1);
        }
    }
    visited[index] = false;
}

int main() {
    int n, m, a, b;

    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }
    for (int i = 0; i < n; i++) {
        solution(i, 0);
        if (ans == true) break;
    }
    cout << ((ans == true) ? 1 : 0);

    return 0;
}
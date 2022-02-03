/**
 * @file 9019.DSLR.cpp
 * @author @devappmin
 * @brief DSLR(골드5)
 * @version 0.1
 * @date 2022-02-02
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

bool visited[10000];
queue<pair<int, string> > q;

void solution(int from, int to) {
    q.push(pair<int, string>(from, ""));

    while (!q.empty()) {
        int num;
        string cmd;
        tie(num, cmd) = q.front();

        q.pop();

        int temp;

        // D
        temp = (num * 2) % 10000;
        if (!visited[temp]) {
            q.push(pair<int, string>(temp, cmd + "D"));
            visited[temp] = true;
            if (temp == to) {
                cout << cmd + "D\n";
                return;
            }
        }

        // S
        temp = (num + 9999) % 10000;
        if (!visited[temp]) {
            q.push(pair<int, string>(temp, cmd + "S"));
            visited[temp] = true;
            if (temp == to) {
                cout << cmd + "S\n";
                return;
            }
        }

        // L
        temp = (num * 10 + num / 1000) % 10000;
        if (!visited[temp]) {
            q.push(pair<int, string>(temp, cmd + "L"));
            visited[temp] = true;
            if (temp == to) {
                cout << cmd + "L\n";
                return;
            }
        }

        // R
        temp = (num + num % 10 * 10000) / 10;
        if (!visited[temp]) {
            q.push(pair<int, string>(temp, cmd + "R"));
            visited[temp] = true;
            if (temp == to) {
                cout << cmd + "R\n";
                return;
            }
        }
    }
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int loop;
    cin >> loop;

    for (int i = 0; i < loop; i++) {
        int from, to;
        cin >> from >> to;
        memset(visited, false, sizeof(visited));
        q = queue<pair<int, string> >();
        solution(from, to);
    }

    return 0;
}
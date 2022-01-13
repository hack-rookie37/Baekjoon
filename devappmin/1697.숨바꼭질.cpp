/**
 * @file 1697.숨바꼭질.cpp
 * @author @devappmin
 * @brief 숨바꼭질(실버1)
 * @version 0.1
 * @date 2022-01-13
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

#define MAX 100005

int world[MAX];

int li[3] = {1, -1, 2};

queue<int> q;

void colonize(int pos) {
    for (int i = 0; i < 3; i++) {
        // 걷기
        if (i != 2 && pos >= 0 && pos <= (MAX - 5)) {
            if (world[pos + li[i]] == 0) {
                world[pos + li[i]] = world[pos] + 1;
                q.push(pos + li[i]);
            }
        } else {  // 뛰기
            if (pos <= (MAX - 5) / 2) {
                if (world[pos * 2] == 0) {
                    world[pos * 2] = world[pos] + 1;
                    q.push(pos * 2);
                }
            }
        }
    }
}

void solution(int n, int k) {
    q.push(n);

    while (world[k] == 0) {
        int pos = q.front();
        q.pop();

        if (pos == k) break;

        colonize(pos);
    }

    cout << world[k] << endl;
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int n, k;
    cin >> n >> k;

    fill(&world[0], &world[MAX], 0);

    solution(n, k);

    return 0;
}
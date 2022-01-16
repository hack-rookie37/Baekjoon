/**
 * @file 17298.오큰수.cpp
 * @author @devappmin
 * @brief 오큰수 (골드4)
 * @version 0.1
 * @date 2022-01-14
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 1000001

using namespace std;

stack<pair<int, int> > s;

int idx[MAX];

void solution(int loop) {
    for (int i = 0; i < loop; i++) {
        int input;
        cin >> input;

        while (!s.empty()) {
            if (s.top().second < input) {
                idx[s.top().first] = input;
                s.pop();
            } else {
                break;
            }
        }

        s.push(pair<int, int>(i, input));
    }

    for (int i = 0; i < loop; i++) {
        cout << idx[i] << " ";
    }
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int loop;
    cin >> loop;

    fill(&idx[0], &idx[loop], -1);

    solution(loop);

    return 0;
}

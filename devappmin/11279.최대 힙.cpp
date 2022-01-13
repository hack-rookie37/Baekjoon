/**
 * @file 11279.최대 힙.cpp
 * @author @devappmin
 * @brief 최대 힙(실버2)
 * @version 0.1
 * @date 2022-01-13
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

priority_queue<int> pq;

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int loop;
    cin >> loop;

    for (int i = 0; i < loop; i++) {
        int input;
        cin >> input;
        if (input == 0) {
            if (pq.empty())
                cout << "0\n";
            else {
                cout << pq.top() << "\n";
                pq.pop();
            }
        } else {
            pq.push(input);
        }
    }

    return 0;
}
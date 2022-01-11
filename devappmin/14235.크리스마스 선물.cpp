/**
 * @file 14235.크리스마스 선물.cpp
 * @author @devappmin
 * @brief 크리스마스 선물 (실버 3)
 * @version 0.1
 * @date 2022-01-11
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>
#include <queue>

using namespace std;

priority_queue<int> pq;

void solution(int n) {
    int input;
    for (int i = 0; i < n; i++) {
        cin >> input;

        if (input == 0) {
            if (pq.empty()) {
                cout << -1 << "\n";
            } else {
                cout << pq.top() << "\n";
                pq.pop();
            }
        } else {
            int val;
            for (int j = 0; j < input; j++) {
                cin >> val;
                pq.push(val);
            }
        }
    }
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int n;
    cin >> n;

    solution(n);

    return 0;
}
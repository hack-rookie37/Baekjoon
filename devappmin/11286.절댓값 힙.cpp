/**
 * @file 11286.절댓값 힙.cpp
 * @author @devappmin
 * @brief 절댓값 힙(실버1)
 * @version 0.1
 * @date 2022-01-13
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>
#include <math.h>

#include <iostream>

using namespace std;

class myComparator {
   public:
    int operator()(const int& p1, const int& p2) {
        if (abs(p1) == abs(p2)) {
            return p1 > p2;
        } else {
            return abs(p1) > abs(p2);
        }
    }
};

priority_queue<int, vector<int>, myComparator> pq;

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
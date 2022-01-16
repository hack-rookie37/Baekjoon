/**
 * @file 1655.가운데를 말해요.cpp
 * @author @devappmin
 * @brief 가운데를 말해요(골드2)
 * @version 0.1
 * @date 2022-01-13
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

priority_queue<int> hf;
priority_queue<int, vector<int>, greater<int> > lf;

void htol() {
    lf.push(hf.top());
    hf.pop();
}

void ltoh() {
    hf.push(lf.top());
    lf.pop();
}

void solution(int loop) {
    for (int i = 0; i < loop; i++) {
        int input;
        cin >> input;

        if (i == 0) {
            hf.push(input);
            cout << hf.top() << "\n";
            continue;
        }

        if (i == 1) {
            if (hf.top() > input) {
                htol();
                hf.push(input);
            } else {
                lf.push(input);
            }
            cout << hf.top() << "\n";
            continue;
        }

        if (input > lf.top()) {
            lf.push(input);
        } else {
            hf.push(input);
        }

        if (hf.size() > lf.size() + 1) {
            htol();
        } else if (hf.size() < lf.size()) {
            ltoh();
        }

        cout << hf.top() << "\n";
    }
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int loop, input;
    cin >> loop;

    solution(loop);

    return 0;
}

// 1
//

// 1
// 5

// 2 1
// 5

// 4 2 1
// 5 10
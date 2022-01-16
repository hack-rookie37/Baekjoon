/**
 * @file 10773.제로.cpp
 * @author @devappmin
 * @brief 제로
 * @version 0.1
 * @date 2022-01-08
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>
#include <stack>

using namespace std;

stack<int> s;

void solution(int len) {
    int input;
    for (int i = 0; i < len; i++) {
        cin >> input;

        if (input == 0)
            s.pop();
        else
            s.push(input);
    }

    int ans = 0;
    while (!s.empty()) {
        ans += s.top();
        s.pop();
    }

    cout << ans;
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int l;
    cin >> l;
    solution(l);

    return 0;
}
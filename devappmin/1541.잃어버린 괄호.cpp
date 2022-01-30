/**
 * @file 1541.잃어버린 괄호.cpp
 * @author @devappmin
 * @brief 잃어버린 괄호(실버2)
 * @version 0.1
 * @date 2022-01-25
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

vector<int> v;

void solution() {
    int ans = 0;
    bool negative = false;
    for (int i = 0; i < v.size(); i++) {
        if (v[i] > 0)
            ans += negative ? -v[i] : v[i];
        else {
            negative = true;
            ans += v[i];
        }
    }
    cout << ans;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    string input;
    cin >> input;

    string temp;
    for (char c : input) {
        temp += c;
        if (c == '-' || c == '+') {
            v.push_back(stoi(temp));
            temp = c;
        }
    }
    v.push_back(stoi(temp));

    solution();

    return 0;
}
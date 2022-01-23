/**
 * @file 1003.피보나치 함수.cpp
 * @author @devappmin
 * @brief 피보나치 함수(실버3)
 * @version 0.1
 * @date 2022-01-21
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>
#define MAX 41
using namespace std;
pair<int, int> called[MAX] = {{1, 0}, {0, 1}};

void solution(int input) {
    for (int i = 2; i <= input; i++) {
        called[i] = {called[i - 1].first + called[i - 2].first, called[i - 1].second + called[i - 2].second};
    }
    cout << called[input].first << " " << called[input].second << "\n";
}

int main() {
    cin.tie(0);
    cout.tie(0);
    cout.sync_with_stdio(0);

    int loop;
    cin >> loop;

    for (int i = 0; i < loop; i++) {
        int input;
        cin >> input;
        solution(input);
    }

    return 0;
}
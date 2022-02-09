/**
 * @file 1463.1로 만들기.cpp
 * @author @devappmin
 * @brief 1로 만들기(실버3)
 * @version 0.1
 * @date 2022-01-24
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 1000001

using namespace std;

int n[MAX];

void solution(int num) {
    n[1] = 0;

    for (int i = 2; i <= num; i++) {
        n[i] = n[i - 1] + 1;
        if (!(i % 3))
            n[i] = min(n[i], n[i / 3] + 1);
        if (!(i % 2))
            n[i] = min(n[i], n[i / 2] + 1);
    }

    cout << n[num];
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int num;
    cin >> num;
    solution(num);

    return 0;
}
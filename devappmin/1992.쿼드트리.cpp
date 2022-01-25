/**
 * @file 1992.쿼드트리.cpp
 * @author @devappmin
 * @brief 쿼드트리(실버1)
 * @version 0.1
 * @date 2022-01-25
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 65

using namespace std;

int arr[MAX][MAX];

void solution(int y, int x, int size) {
    int sv = arr[y][x];

    for (int i = y; i < y + size; i++) {
        for (int j = x; j < x + size; j++) {
            if (arr[i][j] != sv) {
                cout << "(";
                solution(y, x, size / 2);
                solution(y, x + size / 2, size / 2);
                solution(y + size / 2, x, size / 2);
                solution(y + size / 2, x + size / 2, size / 2);
                cout << ")";
                return;
            }
        }
    }

    cout << sv;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        string str;
        cin >> str;
        for (int j = 0; j < n; j++)
            arr[i][j] = str[j] - '0';
    }

    solution(0, 0, n);

    return 0;
}
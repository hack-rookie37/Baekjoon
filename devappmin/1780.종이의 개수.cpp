/**
 * @file 1780.종이의 개수.cpp
 * @author @devappmin
 * @brief 종이의 개수(실버2)
 * @version 0.1
 * @date 2022-01-25
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 2500

using namespace std;

int arr[MAX][MAX];

int sol[3] = {0, 0, 0};

void paper(int x, int y, int size) {
    int basedValue = arr[y][x];

    if (size == 1) {
        sol[basedValue + 1]++;
        return;
    }

    for (int i = y; i < y + size; i++) {
        for (int j = x; j < x + size; j++) {
            if (arr[i][j] != basedValue) {
                for (int a = 0; a < size; a += size / 3)
                    for (int b = 0; b < size; b += size / 3)
                        paper(x + a, y + b, size / 3);
                return;
            }
        }
    }

    sol[basedValue + 1]++;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }

    paper(0, 0, n);

    for (int a : sol)
        cout << a << "\n";

    return 0;
}
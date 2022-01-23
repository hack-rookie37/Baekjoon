/**
 * @file 9184.신나는 함수 실행.cpp
 * @author @devappmin
 * @brief 신나는 함수 실행(실버2)
 * @version 0.1
 * @date 2022-01-23
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

// if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
//     1

// if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
//     w(20, 20, 20)

// if a < b and b < c, then w(a, b, c) returns:
//     w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

// otherwise it returns:
//     w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

#include <bits/stdc++.h>

#include <iostream>

#define MAX 105

#define POS(x) x + 50

using namespace std;

long w[MAX][MAX][MAX];

int main() {
    cin.tie(0);
    cout.tie(0);
    cout.sync_with_stdio(0);

    fill(&w[0][0][0], &w[100][100][100], 1);

    for (int i = -50; i <= 50; i++) {
        for (int j = -50; j <= 50; j++) {
            for (int k = -50; k <= 50; k++) {
                if (i <= 0 || j <= 0 || k <= 0)
                    w[POS(i)][POS(j)][POS(k)] = 1;
                else if (i > 20 || j > 20 || k > 20)
                    w[POS(i)][POS(j)][POS(k)] = 1048576;  // Equals w[POS(20)][POS(20)][POS(20)]
                else if (i < j && j < k)
                    w[POS(i)][POS(j)][POS(k)] = w[POS(i)][POS(j)][POS(k - 1)] + w[POS(i)][POS(j - 1)][POS(k - 1)] - w[POS(i)][POS(j - 1)][POS(k)];
                else
                    w[POS(i)][POS(j)][POS(k)] = w[POS(i - 1)][POS(j)][POS(k)] + w[POS(i - 1)][POS(j - 1)][POS(k)] + w[POS(i - 1)][POS(j)][POS(k - 1)] - w[POS(i - 1)][POS(j - 1)][POS(k - 1)];
            }
        }
    }

    int a, b, c;
    cin >> a >> b >> c;

    while (a != -1 || b != -1 || c != -1) {
        cout << "w(" << a << ", " << b << ", " << c << ") = " << w[POS(a)][POS(b)][POS(c)] << "\n";
        cin >> a >> b >> c;
    }

    return 0;
}
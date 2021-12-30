/**
 * @file 1461.도서관.cpp
 * @author @devappmin
 * @brief 도서관
 * @version 0.1
 * @date 2021-12-30
 *
 * @copyright Copyright (c) 2021 @devappmin
 *
 */

#include <math.h>

#include <algorithm>
#include <iostream>

#define MAX 20002
using namespace std;

int ans = 0;
int books[MAX] = {0};

void solution(int size, int carry) {
    int i, pivot = size;

    for (i = 0; i <= size; i++) {
        if (books[i] == 0) {
            pivot = i;
            break;
        }
    }

    for (i = size; i > pivot; i -= carry)
        ans += books[i] * 2;

    for (i = 0; i < pivot; i += carry)
        ans += abs(books[i]) * 2;

    ans -= max(abs(books[0]), abs(books[size]));

    cout << ans << endl;
}

int main() {
    cout.sync_with_stdio(0);
    cin.tie(0);

    int n, m, i, val;
    cin >> n >> m;

    for (i = 1; i <= n; i++) {
        cin >> books[i];
    }

    sort(books, books + n + 1);

    solution(n, m);
    return 0;
}
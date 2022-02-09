/**
 * @file 1074.Z.cpp
 * @author @devappmin
 * @brief Z (실버1)
 * @version 0.1
 * @date 2022-01-23
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;
int ans = 0;
void z(int y, int x, int ay, int ax, int size) {
    if (y == ay && x == ax) {
        cout << ans;
        return;
    }

    if (ay >= y && ay < y + size && ax >= x && ax < x + size) {
        z(y, x, ay, ax, size / 2);
        z(y, x + size / 2, ay, ax, size / 2);
        z(y + size / 2, x, ay, ax, size / 2);
        z(y + size / 2, x + size / 2, ay, ax, size / 2);
    } else {
        ans += size * size;
    }
}

int main() {
    cin.tie(0);
    cout.tie(0);
    cout.sync_with_stdio(0);

    int n, r, c;
    cin >> n >> r >> c;

    z(0, 0, r, c, pow(2, n));

    return 0;
}
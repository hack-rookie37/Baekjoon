/**
 * @file 1085.직사각형에서 탈출.cpp
 * @author @devappmin
 * @brief 직사각형에서 탈출(브론즈3)
 * @version 0.1
 * @date 2022-01-15
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>

using namespace std;

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int x, y, w, h;

    cin >> x >> y >> w >> h;

    cout << min(min(w - x, x), min(h - y, y));

    return 0;
}
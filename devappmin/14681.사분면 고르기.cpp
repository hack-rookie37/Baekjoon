/**
 * @file 14681.사분면 고르기.cpp
 * @author @devappmin
 * @brief 사분면 고르기(브론즈4)
 * @version 0.1
 * @date 2022-01-14
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>

using namespace std;

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int x, y;
    cin >> x >> y;

    cout << (x > 0 ? y > 0 ? 1 : 4 : y > 0 ? 2
                                           : 3);

    return 0;
}
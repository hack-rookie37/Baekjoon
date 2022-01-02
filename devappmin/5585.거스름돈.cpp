/**
 * @file 5585.거스름돈.cpp
 * @author @devappmin
 * @brief 거스름돈 (브론즈2)
 * @version 0.1
 * @date 2022-01-03
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>

using namespace std;

int change[6] = {500, 100, 50, 10, 5, 1};
int ans = 0;

void solution(int money) {
    for (int i = 0; i < 6; i++) {
        ans += (int)money / change[i];
        money %= change[i];
    }
    cout << ans;
}

int main() {
    int money;
    cin >> money;

    solution(1000 - money);

    return 0;
}
/**
 * @file 1629.곱셈.cpp
 * @author @devappmin
 * @brief 곱셈(실버1)
 * @version 0.1
 * @date 2022-01-26
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

long long a, b, c;

long long mul(long long a, long long b) {
    if (b == 1)
        return a;
    if (b == 0)
        return 1;

    if (b % 2 == 1)
        return mul(a, b - 1) * a;
    else {
        long long temp = mul(a, b / 2);
        temp %= c;
        return (temp * temp) % c;
    }
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    cin >> a >> b >> c;

    cout << mul(a, b) % c;

    return 0;
}

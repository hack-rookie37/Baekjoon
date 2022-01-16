/**
 * @file 10870.피보나치 수 5.cpp
 * @author @devappmin
 * @brief 피보나치 수 5 (브론즈2)
 * @version 0.1
 * @date 2022-01-03
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>

#define MAX 21

using namespace std;

int arr[MAX] = {0, 1};

void solution(int size) {
    for (int i = 2; i <= size; i++) {
        arr[i] = arr[i - 1] + arr[i - 2];
    }
    cout << arr[size];
}

int main() {
    cout.sync_with_stdio(0);
    cin.tie(0);

    int size;

    cin >> size;

    solution(size);

    return 0;
}
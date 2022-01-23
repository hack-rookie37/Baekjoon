/**
 * @file 2750.수 정렬하기.cpp
 * @author @devappmin
 * @brief 수 정렬하기(브론즈1)
 * @version 0.1
 * @date 2022-01-22
 *
 * @copyright Copyriht (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

int main() {
    cin.tie(0);
    cout.tie(0);
    cout.sync_with_stdio(0);
    int l;
    cin >> l;
    int arr[l];
    for (int i = 0; i < l; i++) {
        cin >> arr[i];
    }
    sort(&arr[0], &arr[l]);
    for (int i = 0; i < l; i++) {
        cout << arr[i] << "\n";
    }
}
/**
 * @file 2447.별 찍기 - 10.cpp
 * @author @devappmin
 * @brief 별 찍기 - 10
 * @version 0.1
 * @date 2022-01-01
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>

using namespace std;

void recursion(int input, int i, int j) {
    if (i / input % 3 == 1 && j / input % 3 == 1) {
        cout << ' ';
    } else if (input == 1) {
        cout << '*';
    } else {
        recursion(input / 3, i, j);
    }
}

void solution(int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            recursion(size, i, j);
        }
        cout << '\n';
    }
}

int main() {
    cout.sync_with_stdio(0);
    cin.tie(0);
    int size;
    cin >> size;

    solution(size);

    return 0;
}
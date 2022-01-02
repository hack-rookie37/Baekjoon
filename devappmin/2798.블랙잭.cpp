/**
 * @file 2798.블랙잭.cpp
 * @author @devappmin
 * @brief 블랙잭
 * @version 0.1
 * @date 2022-01-02
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>

using namespace std;

int cards[101];

void solution(int len, int size) {
    int max = 0;

    for (int i = 0; i < len - 2; i++) {
        for (int j = i + 1; j < len - 1; j++) {
            for (int k = j + 1; k < len; k++) {
                if (cards[i] + cards[j] + cards[k] > max && cards[i] + cards[j] + cards[k] <= size)
                    max = cards[i] + cards[j] + cards[k];
            }
        }
    }

    cout << max;
}
int main() {
    int n, m;

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> cards[i];
    }

    solution(n, m);

    return 0;
}
/**
 * @file 9663.N-Queen.cpp
 * @author @devappmin
 * @brief N-Queen
 * @version 0.1
 * @date 2021-12-28
 *
 * @copyright Copyright @devappmin (c) 2021
 *
 */

#include <math.h>

#include <iostream>

using namespace std;

int sol = 0;

bool promising(int index, int* col) {
    int k = 1;
    bool s = true;

    while (k < index && s) {
        if (col[index] == col[k] || abs(col[index] - col[k]) == abs(index - k))
            s = false;
        k++;
    }

    return s;
}

void nqueen(int size, int index, int* col) {
    if (promising(index, col)) {
        if (index == size)
            sol++;
        else {
            for (int i = 0; i < size; i++) {
                col[index + 1] = i;
                nqueen(size, index + 1, col);
            }
        }
    }
}

int main() {
    int size;
    cin >> size;
    int col[size];
    for (int i = 0; i < size; i++) col[i] = 0;
    nqueen(size, 0, col);
    cout << sol << endl;
    return 0;
}
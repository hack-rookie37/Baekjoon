/**
 * @file 10828.스택.cpp
 * @author @devappmin
 * @brief 스택
 * @version 0.1
 * @date 2021-12-29
 *
 * @copyright Copyright (c) 2021 @devappmin
 *
 */

#include <iostream>
#include <string>

using namespace std;

int arr[10001] = {0};

void push(int *pos, int val) {
    arr[++(*pos)] = val;
}

int pop(int *pos) {
    if (*pos == 0) return -1;

    return arr[(*pos)--];
}

int size(int pos) {
    return pos;
}

int empty(int pos) {
    return pos <= 0 ? 1 : 0;
}

int top(int pos) {
    if (pos == 0) return -1;
    return arr[pos];
}

int main() {
    int pos = 0;
    int param;
    int r;
    string cmd;
    string result;

    cin >> r;

    for (int i = 0; i < r; i++) {
        cin >> cmd;
        if (cmd.compare("push") == 0) {
            cin >> param;
            push(&pos, param);
        } else if (cmd.compare("pop") == 0) {
            result += to_string(pop(&pos)) + "\n";
        } else if (cmd.compare("size") == 0) {
            result += to_string(size(pos)) + "\n";
        } else if (cmd.compare("empty") == 0) {
            result += to_string(empty(pos)) + "\n";
        } else if (cmd.compare("top") == 0) {
            result += to_string(top(pos)) + "\n";
        }
    }

    cout << result;

    return 0;
}
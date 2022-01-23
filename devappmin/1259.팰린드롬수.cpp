/**
 * @file 1259.팰린드롬수.cpp
 * @author @devappmin
 * @brief 팰린드롬수(브론즈 1)
 * @version 0.1
 * @date 2022-01-17
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>

using namespace std;

void solution(string input) {
    bool ans = true;

    for (int i = 0; i < input.length() / 2; i++) {
        if (input[i] != input[input.length() - i - 1]) {
            ans = false;
            break;
        }
    }

    cout << (ans ? "yes" : "no")
         << "\n";
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    string input;
    cin >> input;

    while (input != "0") {
        solution(input);
        cin >> input;
    }

    return 0;
}
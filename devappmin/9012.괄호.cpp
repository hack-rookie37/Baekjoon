/**
 * @file 9012.괄호.cpp
 * @author @devappmin
 * @brief 괄호
 * @version 0.1
 * @date 2022-01-06
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>

using namespace std;

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int repeat, check = 0;
    string s;
    cin >> repeat;

    for (int i = 0; i < repeat; i++) {
        cin >> s;

        if (s.length() % 2 != 0) {
            cout << "NO" << endl;
            continue;
        }

        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(')
                check++;
            else
                check--;

            if (check < 0) break;
        }

        if (check == 0)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;

        check = 0;
    }

    return 0;
}
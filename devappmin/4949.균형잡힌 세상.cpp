/**
 * @file 4949.균형잡힌 세상.cpp
 * @author @devappmin
 * @brief 균형잡힌 세상(실버4)
 * @version 0.1
 * @date 2022-01-14
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

string text;

stack<char> s;

void solution() {
    int lcount = 0, hcount = 0;
    bool ans = true;
    for (int i = 0; i < text.length() - 1; i++) {
        switch (text[i]) {
            case '(':
                s.push('(');
                lcount++;
                break;
            case ')':
                if (!s.empty()) {
                    if (s.top() == '[')
                        ans = false;
                    s.pop();
                }

                lcount--;

                break;
            case '[':
                s.push('[');
                hcount++;
                break;
            case ']':
                if (!s.empty()) {
                    if (s.top() == '(')
                        ans = false;
                    s.pop();
                }
                hcount--;
                break;
            case '.':
                if (lcount == 0 && hcount == 0 && ans == true) {
                    cout << "yes\n";
                } else {
                    cout << "no\n";
                }
                lcount = 0;
                hcount = 0;
                ans = true;
                break;
        }

        if (lcount < 0 || hcount < 0)
            ans = false;
    }
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    string str;

    int line = 0;
    do {
        getline(cin, str);
        text += str;
    } while (str != ".");
    solution();

    return 0;
}
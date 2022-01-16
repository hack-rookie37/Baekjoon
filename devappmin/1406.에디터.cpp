/**
 * @file 1406.에디터.cpp
 * @author @devappmin
 * @brief 에디터 (실버3)
 * @version 0.1
 * @date 2022-01-06
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>
#include <list>

using namespace std;

list<char> str;

void solution(int cmdLength) {
    auto cursor = str.end();
    char cmd, input;

    for (int i = 0; i < cmdLength; i++) {
        cin >> cmd;

        switch (cmd) {
            case 'L':
                if (cursor != str.begin())
                    cursor--;
                break;

            case 'D':
                if (cursor != str.end())
                    cursor++;
                break;

            case 'B':
                if (cursor != str.begin()) {
                    cursor--;
                    cursor = str.erase(cursor);
                }
                break;

            case 'P':
                cin >> input;
                str.insert(cursor, input);
                break;
        }
    }
    for (char c : str) {
        cout << c;
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    string input;
    int cmdLength;

    cin >> input >> cmdLength;

    for (char c : input)
        str.push_back(c);

    solution(cmdLength);

    return 0;
}
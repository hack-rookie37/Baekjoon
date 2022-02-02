/**
 * @file 7662.이중 우선순위 큐.cpp
 * @author @devappmin
 * @brief 이중 우선순위 큐 (골드5)
 * @version 0.1
 * @date 2022-01-31
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

void solution(int clength) {
    multiset<int> ms;

    char cmd;
    int val;

    for (int i = 0; i < clength; i++) {
        cin >> cmd >> val;

        switch (cmd) {
            case 'I':
                ms.insert(val);
                break;
            case 'D':
                if (!ms.empty())
                    ms.erase(ms.lower_bound(val == 1 ? *--ms.end() : *ms.begin()));
                break;
        }
    }

    if (ms.empty())
        cout << "EMPTY\n";
    else
        cout << *--ms.end() << " " << *ms.begin() << "\n";
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int loop;
    cin >> loop;

    for (int i = 0; i < loop; i++) {
        int cmd;
        cin >> cmd;
        solution(cmd);
    }

    return 0;
}

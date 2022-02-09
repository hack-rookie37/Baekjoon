/**
 * @file 5525.IOIOI.cpp
 * @author @devappmin
 * @brief IOIOI (실버3)
 * @version 0.1
 * @date 2022-02-02
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

void solution(int n, int m, string s) {
    int ans = 0;

    for (int i = 0; i < m; i++) {
        if (s[i] == 'O')
            continue;
        else {
            int cnt = 0;
            while (s[i + 1] == 'O' && s[i + 2] == 'I') {
                cnt++;
                if (cnt == n) {
                    cnt--;
                    ans++;
                }
                i += 2;
            }
        }
    }

    cout << ans;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int n, m;
    string s;

    cin >> n >> m >> s;

    solution(n, m, s);

    return 0;
}
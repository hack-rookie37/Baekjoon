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
    string ioi = "";

    for (int i = 0; i < n; i++) {
        ioi += "IO";
    }
    ioi += "I";

    string::size_type pos = 0;
    while ((pos = s.find(ioi, pos)) != string::npos) {
        ans++;
        pos += 2;
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
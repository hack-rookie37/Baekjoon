/**
 * @file 1764.듣보잡.cpp
 * @author @devappmin
 * @brief 듣보잡 (실버4)
 * @version 0.1
 * @date 2022-01-25
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

set<string> s;
vector<string> ans;
int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int n, m;
    string input;

    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> input;
        s.insert(input);
    }

    int sz = s.size(), dsz = 0;
    for (int i = 0; i < m; i++) {
        cin >> input;
        s.insert(input);
        dsz = s.size();

        if (dsz == sz) {
            ans.push_back(input);
        }
        sz = dsz;
    }
    cout << ans.size() << "\n";
    sort(ans.begin(), ans.end());
    for (string a : ans)
        cout << a << "\n";

    return 0;
}
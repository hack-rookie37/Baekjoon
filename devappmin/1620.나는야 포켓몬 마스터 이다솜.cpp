/**
 * @file 1620.나는야 포켓몬 마스터 이다솜.cpp
 * @author @devappmin
 * @brief 나는야 포켓몬 마스터 이다솜(실버4)
 * @version 0.1
 * @date 2022-01-17
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

map<int, string> pokemon_i;
map<string, int> pokemon_s;

bool isNumber(const string s) {
    return s[0] >= '0' && s[0] <= '9';
}

void solution(string input) {
    if (isNumber(input)) {
        cout << pokemon_i[stoi(input)] << "\n";
    } else {
        cout << pokemon_s[input] << "\n";
    }
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int m, n;
    string name;
    cin >> m >> n;

    for (int i = 1; i <= m; i++) {
        cin >> name;
        pokemon_i.insert({i, name});
        pokemon_s.insert({name, i});
    }

    for (int i = 0; i < n; i++) {
        cin >> name;
        solution(name);
    }

    return 0;
}
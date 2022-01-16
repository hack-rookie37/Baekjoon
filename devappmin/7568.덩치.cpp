/**
 * @file 7568.덩치.cpp
 * @author @devappmin
 * @brief 덩치
 * @version 0.1
 * @date 2021-12-29
 *
 * @copyright Copyright @devappmin (c) 2021
 *
 */

#include <iostream>
#include <utility>
#include <vector>

using namespace std;

void solution(int n, vector<pair<int, int> > v) {
    int rank = 1;
    for (int i = 0; i < n; i++) {
        rank = 1;
        for (int j = 0; j < n; j++) {
            if (i == j) continue;

            if (v[i].first < v[j].first && v[i].second < v[j].second)
                rank++;
        }
        cout << rank;
        if (i != n - 1)
            cout << ' ';
    }
}

int main() {
    int n;
    cin >> n;

    vector<pair<int, int> > v;

    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        v.push_back(pair<int, int>(a, b));
    }

    solution(n, v);
    return 0;
}
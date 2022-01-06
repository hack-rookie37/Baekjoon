/**
 * @file 1759.암호 만들기.cpp
 * @author @devappmin
 * @brief 암호 만들기 (골드5)
 * @version 0.1
 * @date 2022-01-04
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

// prev_permutation을 이용하여 문자열 조합을 구할 수 있음.

#include <algorithm>
#include <iostream>
#include <vector>

#define MAX 20

using namespace std;

char arr[MAX];
bool check[MAX];

char ms[5] = {'a', 'e', 'i', 'o', 'u'};

void solution(int l, int c) {
    do {
        int j = 0, m = 0;
        vector<char> v;
        for (int i = 0; i < c; i++) {
            if (check[i]) {
                for (char t : ms) {
                    if (arr[i] == t) {
                        m++;
                        break;
                    }
                }
                v.push_back(arr[i]);
            }
        }

        j = l - m;

        if (j >= 2 && m >= 1) {
            for (int i = 0; i < v.size(); i++) {
                cout << v[i];
            }
            cout << endl;
        }
    } while (prev_permutation(check, check + c));
}

int main() {
    cout.sync_with_stdio(0);
    cin.tie(0);

    int l, c;

    cin >> l >> c;

    for (int i = 0; i < c; i++) {
        cin >> arr[i];

        if (i < l)
            check[i] = true;
    }

    sort(arr, arr + c);

    solution(l, c);

    return 0;
}
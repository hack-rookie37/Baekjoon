/**
 * @file 2805.나무 자르기.cpp
 * @author @devappmin
 * @brief 나무 자르기(실버3)
 * @version 0.1
 * @date 2022-01-03
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <math.h>

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<long long> arr;
long long ans, save = 0;

void solution(long long length, long long sol) {
    long long i = length - 1, cnt = 1;
    ans = arr[i];

    while (save < sol && i > 0) {
        save += cnt++ * (arr[i] - arr[i - 1]);
        ans = arr[i - 1];
        i--;
    }

    if (save > sol)
        ans += abs(save - sol) / (cnt - 1);
    else if (save < sol)
        ans -= (double)(sol - save) / cnt;

    cout << ans << endl;
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    long long n, m, i, input;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        cin >> input;
        arr.push_back(input);
    }

    sort(arr.begin(), arr.end());

    solution(n, m);
    return 0;
}
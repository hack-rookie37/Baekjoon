/**
 * @file 9251.LCS.cpp
 * @author @devappmin
 * @brief LCS (골드5)
 * @version 0.1
 * @date 2022-01-21
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 * LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
 * 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.
 *
 * 첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.
 *
 *
 * 첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
 *
 */

#pragma region HINT

/**
 * 만약, 비교하는 위치의 문자가 서로 같으면
 * 현재 위치의 값 = 왼쪽 대각선 값 + 1  (배열 범위를 벗어났으면 0이라고 가정 )
 * 다르다면
 * 현재 위치의 값 = MAX{왼쪽 값, 위쪽 값}
 */

#pragma endregion

#include <bits/stdc++.h>

#include <iostream>

#define MAX 1001

using namespace std;

void solution(string sa, string sb) {
    int lcs[MAX][MAX];
    fill(&lcs[0][0], &lcs[0][sb.length() + 1], 0);

    int i, j;
    for (i = 1; i <= sa.length(); i++) {
        for (j = 1; j <= sb.length(); j++) {
            if (sa[i - 1] == sb[j - 1])
                lcs[i][j] = lcs[i - 1][j - 1] + 1;
            else
                lcs[i][j] = max(lcs[i][j - 1], lcs[i - 1][j]);
        }
    }
    cout << lcs[i - 1][j - 1];
}

int main() {
    cin.tie(0);
    cout.tie(0);
    cout.sync_with_stdio(0);

    string sa, sb;

    cin >> sa >> sb;

    solution(sa, sb);

    return 0;
}
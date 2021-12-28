/**
 * @file 1920.수 찾기.cpp
 * @author @devappmin
 * @brief 수 찾기
 * @version 0.1
 * @date 2021-12-28
 *
 * @copyright Copyright @devappmin (c) 2021
 *
 */

// cin, cout은 처리 속도가 느리므로 가능하면 printf나 scanf를 사용하자.

#include <algorithm>
#include <iostream>

using namespace std;

void selection(int* A, int start, int end, int search) {
    int mid;
    while (start <= end) {
        mid = (start + end) / 2;
        if (A[mid] > search)
            end = mid - 1;
        else if (A[mid] < search)
            start = mid + 1;
        else {
            printf("1\n");
            return;
        }
    }

    printf("0\n");
}

void solution() {
    int n, m, i;

    scanf("%d", &n);
    int A[n];

    for (i = 0; i < n; i++)
        scanf("%d", &A[i]);

    scanf("%d", &m);
    int B[m];

    for (i = 0; i < m; i++)
        scanf("%d", &B[i]);

    sort(A, A + n);

    for (i = 0; i < m; i++)
        selection(A, 0, n - 1, B[i]);
}

int main() {
    solution();
    return 0;
}
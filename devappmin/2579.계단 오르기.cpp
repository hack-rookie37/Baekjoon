#include <iostream>

using namespace std;

#define MAX 309

int dp[MAX];
int arr[MAX];

void solution(int size) {
    dp[0] = arr[0];
    dp[1] = arr[0] + arr[1];
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2]);

    for (int i = 3; i < size; i++) {
        dp[i] = max(dp[i - 2] + arr[i], dp[i - 3] + arr[i - 1] + arr[i]);
    }

    cout << dp[size - 1];
}

int main() {
    cin.tie(0);
    cout.tie(0);
    ios_base::sync_with_stdio(0);

    int count;
    cin >> count;

    for (int i = 0; i < count; i++) {
        cin >> arr[i];
    }

    solution(count);

    return 0;
}

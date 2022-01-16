/**
 * @file 2493.탑.cpp
 * @author @devappmin
 * @brief 탑
 * @version 0.1
 * @date 2022-01-08
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>
#include <stack>

using namespace std;

stack<pair<int, int> > s;

void solution(int l) {
    int input;
    for (int i = 1; i <= l; i++) {
        scanf("%d", &input);

        while (!s.empty()) {
            if (s.top().second > input) {
                printf("%d ", s.top().first);
                break;
            }
            s.pop();
        }

        if (s.empty()) {
            printf("0 ");
        }

        s.push(pair<int, int>(i, input));
    }
}

int main() {
    int l;
    scanf("%d", &l);
    solution(l);
    return 0;
}

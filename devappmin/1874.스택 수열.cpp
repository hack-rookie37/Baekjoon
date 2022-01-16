/**
 * @file 1874.스택 수열.cpp
 * @author your name (you@domain.com)
 * @brief
 * @version 0.1
 * @date 2022-01-10
 *
 * @copyright Copyright (c) 2022
 *
 */

#include <iostream>
#include <stack>
#include <vector>

using namespace std;

stack<int> sa;
string ans;
bool popped[100001];

void solution(int len) {
    int before = 1, input;
    bool b = true;

    for (int j = 0; j < len; j++) {
        scanf("%d", &input);

        if (input > len) {
            b = false;
            continue;
        }
        if (popped[input] == true) {
            b = false;
            continue;
        }

        if (input >= before) {
            for (int i = before; i <= input; i++) {
                sa.push(i);
                popped[i] = false;
                ans += '+';
            }
            popped[sa.top()] = true;
            sa.pop();
            ans += '-';

            before = input + 1;
        } else {
            while (!sa.empty()) {
                if (sa.top() == input) {
                    popped[sa.top()] = true;
                    sa.pop();
                    ans += "-";
                    break;
                }

                popped[sa.top()] = true;
                sa.pop();
            }
        }
    }

    if (b)
        for (auto c : ans)
            printf("%c\n", c);
    else
        cout << "NO";
}

int main() {
    int l;
    scanf("%d", &l);
    solution(l);

    return 0;
}
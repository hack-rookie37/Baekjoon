/**
 * @file 1927.최소힙.cpp
 * @author @devappmin
 * @brief 최소힙
 * @version 0.1
 * @date 2022-01-06
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>
#include <queue>

using namespace std;

priority_queue<int, vector<int>, greater<int> > pq;

void solution(int loop) {
    int input;
    for (int i = 0; i < loop; i++) {
        scanf("%d", &input);

        if (input == 0) {
            if (pq.size() == 0)
                printf("0\n");
            else {
                printf("%d\n", pq.top());
                pq.pop();
            }
        } else {
            pq.push(input);
        }
    }
}

int main() {
    int loop;
    scanf("%d", &loop);

    solution(loop);

    return 0;
}
/**
 * @file 3190.뱀.cpp
 * @author @devappmin
 * @brief 뱀(골드5)
 * @version 0.1
 * @date 2022-01-16
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <bits/stdc++.h>

#include <iostream>

#define MAX 105

using namespace std;

int world[MAX][MAX];

vector<pair<int, char> > cmds;
deque<pair<int, int> > sk;

const int APPLE = 2;
const int WALL = -2;
const int SNAKE = 1;
const int EMPTY = 0;

int li[2][4] = {{0, 1, 0, -1}, {1, 0, -1, 0}};

void solution(int size) {
    sk.push_back(pair<int, int>(1, 1));
    world[1][1] = 1;
    int rotate = 0;
    int move = 0;
    int bf = 0;

    bool ans = true;

    for (pair<int, char> cmd : cmds) {
        for (int i = 0; i < cmd.first - bf; i++) {
            int x, y;
            tie(y, x) = sk.front();

            if (world[y + li[0][rotate]][x + li[1][rotate]] == APPLE) {
                sk.push_front(pair<int, int>(y + li[0][rotate], x + li[1][rotate]));
                world[y + li[0][rotate]][x + li[1][rotate]] = SNAKE;
                move++;
            } else if (world[y + li[0][rotate]][x + li[1][rotate]] == EMPTY) {
                sk.push_front(pair<int, int>(y + li[0][rotate], x + li[1][rotate]));
                world[y + li[0][rotate]][x + li[1][rotate]] = SNAKE;
                world[sk.back().first][sk.back().second] = 0;
                sk.pop_back();
                move++;
            } else {
                ans = false;
                break;
            }
            // cout << endl;
            // for (int j = 1; j <= size; j++) {
            //     for (int k = 1; k <= size; k++) {
            //         cout << world[j][k] << " ";
            //     }
            //     cout << endl;
            // }
        }
        bf = cmd.first;
        // cout << rotate << endl;
        if (cmd.second == 'D')
            rotate == 3 ? rotate = 0 : rotate++;
        else if (cmd.second == 'L')
            rotate == 0 ? rotate = 3 : rotate--;

        if (!ans)
            break;
    }

    cout << move + 1;
}

int main() {
    cin.tie(0);
    cout.sync_with_stdio(0);

    int size, appleCount;
    cin >> size >> appleCount;

    fill(&world[0][0], &world[size + 2][size + 2] + 1, WALL);

    for (int i = 1; i <= size; i++)
        for (int j = 1; j <= size; j++)
            world[i][j] = EMPTY;

    for (int i = 0; i < appleCount; i++) {
        int x, y;
        cin >> y >> x;
        world[y][x] = APPLE;
    }

    int cmdCount;
    cin >> cmdCount;

    for (int i = 0; i < cmdCount; i++) {
        int a;
        char b;
        cin >> a >> b;
        cmds.push_back(pair<int, int>(a, b));
    }
    cmds.push_back(pair<int, int>(105, 'D'));

    solution(size);

    return 0;
}

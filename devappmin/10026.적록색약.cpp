/**
 * @file 10026.적록색약.cpp
 * @author @devappmin
 * @brief 적록색약
 * @version 0.1
 * @date 2022-01-01
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 */

#include <iostream>
#include <queue>
#include <utility>

using namespace std;

pair<char, bool> rgbMap[102][102];
pair<char, bool> gbMap[102][102];

int ans1 = 1, ans2 = 1;

int li[2][4] = {{-1, 1, 0, 0}, {0, 0, -1, 1}};

queue<pair<int, int> > q;
queue<pair<int, int> > nextQ;

void colonize(char c, int y, int x) {
    for (int i = 0; i < 4; i++) {
        if (rgbMap[y + li[0][i]][x + li[1][i]].second == false) {
            if (rgbMap[y + li[0][i]][x + li[1][i]].first == c) {
                rgbMap[y + li[0][i]][x + li[1][i]].second = true;
                q.push(pair<int, int>(y + li[0][i], x + li[1][i]));
            } else if (rgbMap[y + li[0][i]][x + li[1][i]].first != '#') {
                nextQ.push(pair<int, int>(y + li[0][i], x + li[1][i]));
            }
        }
    }
}

void colonizeGB(char c, int y, int x) {
    for (int i = 0; i < 4; i++) {
        if (gbMap[y + li[0][i]][x + li[1][i]].second == false) {
            if (gbMap[y + li[0][i]][x + li[1][i]].first == c) {
                gbMap[y + li[0][i]][x + li[1][i]].second = true;
                q.push(pair<int, int>(y + li[0][i], x + li[1][i]));
            } else if (gbMap[y + li[0][i]][x + li[1][i]].first != '#') {
                nextQ.push(pair<int, int>(y + li[0][i], x + li[1][i]));
            }
        }
    }
}

void solution() {
    q.push(pair<int, int>(1, 1));

    while (!q.empty()) {
        pair<int, int> pos = q.front();
        rgbMap[pos.first][pos.second].second = true;
        q.pop();

        colonize(rgbMap[pos.first][pos.second].first, pos.first, pos.second);

        if (q.empty() && !nextQ.empty()) {
            q.push(nextQ.front());
            if (rgbMap[nextQ.front().first][nextQ.front().second].second == false)
                ans1++;
            nextQ.pop();
        }
    }

    q.push(pair<int, int>(1, 1));
    nextQ = queue<pair<int, int> >();

    while (!q.empty()) {
        pair<int, int> pos = q.front();
        gbMap[pos.first][pos.second].second = true;
        q.pop();

        colonizeGB(gbMap[pos.first][pos.second].first, pos.first, pos.second);

        if (q.empty() && !nextQ.empty()) {
            q.push(nextQ.front());
            if (gbMap[nextQ.front().first][nextQ.front().second].second == false)
                ans2++;
            nextQ.pop();
        }
    }
}

int main() {
    cout.sync_with_stdio(0);
    cin.tie(0);

    int size;
    char input;

    cin >> size;

    for (int i = 0; i <= size + 1; i++) {
        for (int j = 0; j <= size + 1; j++) {
            if (i == 0 || i == size + 1 || j == 0 || j == size + 1) {
                rgbMap[i][j] = pair<char, bool>('#', true);
                gbMap[i][j] = pair<char, bool>('#', true);
            } else {
                cin >> input;
                rgbMap[i][j] = pair<char, bool>(input, false);

                if (input == 'G')
                    input = 'R';
                gbMap[i][j] = pair<char, bool>(input, false);
            }
        }
    }

    solution();

    cout << ans1 << ' ' << ans2 << endl;

    return 0;
}
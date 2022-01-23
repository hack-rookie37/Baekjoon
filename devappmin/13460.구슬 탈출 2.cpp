/**
 * @file 13460.구슬 탈출 2.cpp
 * @author @devappmin
 * @brief 구슬 탈출 2(골드1)
 * @version 0.1
 * @date 2022-01-19
 *
 * @copyright Copyright (c) 2022 @devappmin
 *
 *
 * 스타트링크에서 판매하는 어린이용 장난감 중에서 가장 인기가 많은 제품은 구슬 탈출이다.
 * 구슬 탈출은 직사각형 보드에 빨간 구슬과 파란 구슬을 하나씩 넣은 다음, 빨간 구슬을 구멍을 통해 빼내는 게임이다.
 * 보드의 세로 크기는 N, 가로 크기는 M이고, 편의상 1×1크기의 칸으로 나누어져 있다. 가장 바깥 행과 열은 모두 막혀져 있고, 보드에는 구멍이 하나 있다.
 * 빨간 구슬과 파란 구슬의 크기는 보드에서 1×1크기의 칸을 가득 채우는 사이즈이고, 각각 하나씩 들어가 있다.
 * 게임의 목표는 빨간 구슬을 구멍을 통해서 빼내는 것이다.이때, 파란 구슬이 구멍에 들어가면 안 된다.
 * 이때, 구슬을 손으로 건드릴 수는 없고, 중력을 이용해서 이리 저리 굴려야 한다.
 * 왼쪽으로 기울이기, 오른쪽으로 기울이기, 위쪽으로 기울이기, 아래쪽으로 기울이기와 같은 네 가지 동작이 가능하다.
 * 각각의 동작에서 공은 동시에 움직인다. 빨간 구슬이 구멍에 빠지면 성공이지만, 파란 구슬이 구멍에 빠지면 실패이다.
 * 빨간 구슬과 파란 구슬이 동시에 구멍에 빠져도 실패이다. 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없다.
 * 또, 빨간 구슬과 파란 구슬의 크기는 한 칸을 모두 차지한다. 기울이는 동작을 그만하는 것은 더 이상 구슬이 움직이지 않을 때 까지이다.
 * 보드의 상태가 주어졌을 때, 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하는 프로그램을 작성하시오.
 *
 * 첫 번째 줄에는 보드의 세로, 가로 크기를 의미하는 두 정수 N, M (3 ≤ N, M ≤ 10)이 주어진다. 다음 N개의 줄에 보드의 모양을 나타내는 길이 M의 문자열이 주어진다.
 * 이 문자열은 '.', '#', 'O', 'R', 'B' 로 이루어져 있다. '.'은 빈 칸을 의미하고, '#'은 공이 이동할 수 없는 장애물 또는 벽을 의미하며, 'O'는 구멍의 위치를 의미한다.
 * 'R'은 빨간 구슬의 위치, 'B'는 파란 구슬의 위치이다.
 * 입력되는 모든 보드의 가장자리에는 모두 '#'이 있다. 구멍의 개수는 한 개 이며, 빨간 구슬과 파란 구슬은 항상 1개가 주어진다.
 *
 * 최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 출력한다. 만약, 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다.
 */

#include <bits/stdc++.h>

#include <iostream>

using namespace std;

#define MAX 15

char world[MAX][MAX];

int visited[MAX][MAX][MAX][MAX];

queue<tuple<int, int, int, int> > q;

int li[2][4] = {{1, -1, 0, 0}, {0, 0, 1, -1}};

bool hole = false;

int move(int rx, int ry, int bx, int by, int oy, int ox) {
    for (int i = 0; i < 4; i++) {
        bool rHole = false, bHole = false;
        int drx = li[1][i], dry = li[0][i], dbx = li[1][i], dby = li[0][i];

        world[ry][rx] = '.', world[by][bx] = '.';
        while ((world[ry + dry][rx + drx] == '.' || world[ry + dry][rx + drx] == 'O') ||
               (world[by + dby][bx + dbx] == '.' || world[by + dby][bx + dbx] == 'O')) {
            if (world[ry + dry][rx + drx] != '#' && world[ry + dry][rx + drx] != 'B') {
                if (world[ry + dry][rx + drx] == 'O') {
                    rHole = true;

                    if (bHole == true)
                        break;
                }
                dry += li[0][i], drx += li[1][i];

                if ((world[ry + dry][rx + drx] == '#' || world[ry + dry][rx + drx] == 'B') && world[ry + dry - li[0][i]][rx + drx - li[1][i]] != 'O')
                    world[ry + dry - li[0][i]][rx + drx - li[1][i]] = 'R';
            }

            if (world[by + dby][bx + dbx] != '#' && world[by + dby][bx + dbx] != 'R') {
                if (world[by + dby][bx + dbx] == 'O') {
                    bHole = true;
                    break;
                }
                dby += li[0][i], dbx += li[1][i];

                if ((world[by + dby][bx + dbx] == '#' || world[by + dby][bx + dbx] == 'R') && world[by + dby - li[0][i]][bx + dbx - li[1][i]] != 'O')
                    world[by + dby - li[0][i]][bx + dbx - li[1][i]] = 'B';
            }

            if (ry + dry == by + dby && rx + drx == bx + dbx) {
                if (li[0][i] + li[1][i] > 0) {
                    ry + rx > by + bx ? (dby -= li[0][i], dbx -= li[1][i]) : (dry -= li[0][i], drx -= li[1][i]);
                } else {
                    ry + rx > by + bx ? (dry -= li[0][i], drx -= li[1][i]) : (dby -= li[0][i], dbx -= li[1][i]);
                }
            }
        }

        world[ry + dry - li[0][i]][rx + drx - li[1][i]] = '.';
        world[by + dby - li[0][i]][bx + dbx - li[1][i]] = '.';
        world[oy][ox] = 'O';

        if (visited[ry + dry - li[0][i]][rx + drx - li[1][i]][by + dby - li[0][i]][bx + dbx - li[1][i]] == 0 && bHole == false) {
            q.push(tuple<int, int, int, int>(ry + dry - li[0][i], rx + drx - li[1][i], by + dby - li[0][i], bx + dbx - li[1][i]));
            visited[ry + dry - li[0][i]][rx + drx - li[1][i]][by + dby - li[0][i]][bx + dbx - li[1][i]] = visited[ry][rx][by][bx] + 1;
        }

        if (rHole == true && bHole == false) {
            hole = true;
            return visited[ry][rx][by][bx] + 1;
        }
    }

    return 0;
}

void solution(int iry, int irx, int iby, int ibx, int oy, int ox) {
    int ans = 0;

    visited[iry][irx][iby][ibx] = 1;
    q.push(tuple<int, int, int, int>(iry, irx, iby, ibx));

    while (!q.empty()) {
        int ry, rx, by, bx;
        tie(ry, rx, by, bx) = q.front();
        q.pop();

        int result = move(rx, ry, bx, by, oy, ox);

        if (result >= 1) {
            ans = result;
            hole = true;
            break;
        } else if (result == -1 || result == -2) {
            hole = false;
        }
    }

    if (hole && ans <= 11)
        cout << ans - 1;
    else
        cout << -1;
}

int main() {
    cin.tie(0);
    cout.tie(0);
    cout.sync_with_stdio(0);

    int n, m;
    cin >> n >> m;

    int ry, rx, by, bx, oy, ox;

    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < m; j++) {
            world[i][j] = s[j];
            if (world[i][j] == 'R') {
                ry = i;
                rx = j;
            }
            if (world[i][j] == 'B') {
                by = i;
                bx = j;
            }
            if (world[i][j] == 'O') {
                oy = i;
                ox = j;
            }
        }
    }

    fill(&visited[0][0][0][0], &visited[n][m][n][m] + 1, 0);

    solution(ry, rx, by, bx, oy, ox);

    return 0;
}

// 10 10

// ##########
// ####..#.##
// #.##.##..#
// #...###.##
// #.#.....##
// ##.....###
// ##.B#...##
// #.#......#
// #..R#.O..#
// ##########
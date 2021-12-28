/**
 * @file 1260.cpp
 * @author @devappmin
 * @brief BFS와 DFS
 * @version 0.1
 * @date 2021-12-28
 *
 * @copyright Copyright @devappmin (c) 2021
 *
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

void dfs(vector<pair<int, int> > v, int s) {
    vector<int> t;
    stack<int> st;

    st.push(s);

    while (!st.empty()) {
        bool b = false;
        int c = st.top();

        for (int i = 0; i < t.size(); i++) {
            if (c == t[i]) {
                b = true;
                break;
            }
        }

        if (b) {
            st.pop();
            continue;
        }

        t.push_back(c);
        st.pop();

        stack<int> tm;
        for (int i = 0; i < v.size(); i++) {
            bool include = false;
            if (v[i].first == c) {
                for (int j = 0; j < t.size(); j++) {
                    if (v[i].second == t[j]) {
                        include = true;
                        break;
                    }
                }
                if (!include) {
                    tm.push(v[i].second);
                    v.erase(v.begin() + i--);
                }
            } else if (v[i].second == c) {
                for (int j = 0; j < t.size(); j++) {
                    if (v[i].first == t[j]) {
                        include = true;
                        break;
                    }
                }
                if (!include) {
                    tm.push(v[i].first);
                    v.erase(v.begin() + i--);
                }
            }
        }

        while (!tm.empty()) {
            st.push(tm.top());
            tm.pop();
        }
    }

    for (int i = 0; i < t.size(); i++) {
        cout << t.at(i);
        if (i != t.size() - 1)
            cout << ' ';
    }
}

void bfs(vector<pair<int, int> > v, int s) {
    vector<int> t;
    queue<int> q;

    q.push(s);
    t.push_back(s);

    while (!q.empty()) {
        int c = q.front();
        q.pop();

        for (int i = 0; i < v.size(); i++) {
            if (v.at(i).first == c) {
                bool include = false;
                for (int j = 0; j < t.size(); j++) {
                    if (v.at(i).second == t.at(j))
                        include = true;
                }

                if (!include) {
                    q.push(v.at(i).second);
                    t.push_back(v.at(i).second);
                    v.erase(v.begin() + i--);
                }
            } else if (v.at(i).second == c) {
                bool include = false;
                for (int j = 0; j < t.size(); j++) {
                    if (v.at(i).first == t.at(j))
                        include = true;
                }

                if (!include) {
                    q.push(v.at(i).first);
                    t.push_back(v.at(i).first);
                    v.erase(v.begin() + i--);
                }
            }
        }
    }

    for (int i = 0; i < t.size(); i++) {
        cout << t.at(i);
        if (i != t.size() - 1)
            cout << ' ';
    }
}

void solution() {
    int n;
    int m;
    int s;
    cin >> n >> m >> s;

    vector<pair<int, int> > v;

    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        if (a < b)
            v.push_back(pair<int, int>(a, b));
        else
            v.push_back(pair<int, int>(b, a));
    }
    sort(v.begin(), v.end());

    dfs(v, s);
    cout << endl;
    bfs(v, s);
}

int main() {
    solution();
    return 0;
}
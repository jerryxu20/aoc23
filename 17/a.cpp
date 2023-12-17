#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<vi> vii;

template<class T> using PQ = priority_queue<T>;
template<class T> using PQG = priority_queue<T, vector<T>, greater<T>>;

#define rep(i, a, b) for (int i=a; i<(b); i++)
#define trav(x,A) for (auto& x : A)

#define sz(x) (int)(x).size()
#define mp make_pair
#define pb push_back


const int MOD = 1000000007;
const char nl = '\n';
int solve(int tt) {
    vii grid;
    string s;
    while(cin >> s) {
        grid.pb({});
        trav(c, s) {
            grid.back().pb(c - '0');
        }
    }

    int n = sz(grid);
    int m = sz(grid[0]);

    // cost, steps, i, j, dir
    PQG<tuple<int, int, int, int, int>> pq;
    pq.push({0, 0, 0, 0, 1});
    pq.push({0, 0, 0, 0, 1});
    pq.push({0, 0, 0, 0, 2});
    pq.push({0, 0, 0, 0, 3});

    map<tuple<int, int, int, int>, int> distance;
    distance[{0, 0, 0, 0}] = 0;
    distance[{0, 0, 0, 1}] = 0;
    distance[{0, 0, 0, 2}] = 0;
    distance[{0, 0, 0, 3}] = 0;

    vector<pi> delta = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    while(sz(pq)) {
        auto [dis, steps, i, j, dir] = pq.top();
        auto [a, b] = delta[dir];
        pq.pop();
        if (i == n - 1 && j == m - 1) {
            cout << dis + grid[i][j] - grid[0][0]<< endl;
            return 0;
        }

        if (distance[{i, j, steps, dir}] != dis) continue;
        int ii, jj;
        int cost = dis + grid[i][j];
        if (steps < 2) {
            ii = i + a;
            jj = j + b;
            tuple<int, int, int, int> nxt = {ii, jj, steps + 1, dir};
            if (ii < 0 || jj < 0 || ii >= n || jj >= m || (distance.count(nxt) && distance[nxt] <= cost)) {

            } else {
                pq.push({cost, steps + 1, ii, jj, dir});
                distance[nxt] = cost;
            }
        }

        rep(x, 0, 4) {
            auto [aa, bb] = delta[x];
            if (delta[x] == delta[dir]) continue;
            if (mp(-aa, -bb) == delta[dir]) continue;
            ii = i + aa;
            jj = j + bb;
            tuple<int, int, int, int> nxt = {ii, jj, 0, x};
            if (ii < 0 || jj < 0 || ii >= n || jj >= m || (distance.count(nxt) && distance[nxt] <= cost)) continue;

            pq.push({cost, 0, ii, jj, x});
            distance[nxt] = cost;
        }
    }

    tt++;
    return 0;
}

int main() {

    int T = 1;
    // cin >> T;
    for (int i = 1; i <= T; i++) {
        if (solve(i)) break;
    }
    T++;
    return 0;
}
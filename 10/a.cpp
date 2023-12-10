#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

typedef pair<int, int> pi;

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vi> vii;
typedef vector<pi> vpi;

#define rep(i, a, b) for (int i=a; i<(b); i++)
#define trav(x,A) for (auto& x : A)

#define sz(x) (int)(x).size()
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back

int n, m;
int id(int i, int j) {
    return i * m + j;
}

vpi connect (char c) {
    if (c == '|') {
        return {{-1, 0}, {1, 0}};
    }
    if (c == '-') {
        return {{0, 1}, {0, -1}};
    }
    if (c == 'L') {
        return {{-1, 0}, {0, 1}};
    }
    if (c == 'J') {
        return {{-1, 0}, {0, -1}};
    }
    if (c == '7') {
        return {{1, 0}, {0, -1}};
    }
    if (c == 'F') {
        return {{1, 0}, {0, 1}};
    }
    return {};
}

vi color;
vi parent;
pi S;
int start;
bool dfs(vii &adj, int node, int par) {
    color[node] = 1;
    for (auto &nxt: adj[node]) {
        if (nxt == par) continue;
        if (color[nxt] == 2) continue;
        parent[nxt] = node;
        if (color[nxt] == 1) return false;
        if (dfs(adj, nxt, node) == false) return false;
    }
    color[node] = 2;
    return true;
}

bool loop(vii &adj) {
    color.assign(n * m, 0);
    parent.assign(n * m, -1);

    if (dfs(adj, start, -1) == false) return true;
    return false;
}

vi bfs(vii &adj) {
    vector<int> dis(n * m, INT_MAX);
    dis[start] = 0;
    queue<int> q;
    q.push(start);

    int ans = 0;
    while(true) {
        int z = sz(q);
        if (z == 0) break;
        while(z--) {
            auto node = q.front();
            q.pop();
            trav(nxt, adj[node]) {
                if (dis[nxt] != INT_MAX) continue;
                dis[nxt] = ans + 1;
                q.push(nxt);
            }
        }
        ans++;
    }
    return dis;
}

int solve() {
    vs grid;
    string s;
    while(cin >> s) {
        grid.pb(s);
    }
    n = sz(grid);
    m = sz(grid[0]);

    vii adj(n * m);

    set<pi> edges;
    rep(i, 0, n) {
        rep(j, 0, m) {
            if (grid[i][j] == 'S') {
                S = {i, j};
                continue;
            }

            vpi dir = connect(grid[i][j]);
            for (auto &[a, b]: dir) {
                int ii = i + a;
                int jj = j + b;
                if (ii < 0 || jj < 0 || ii >= n || jj >= m) continue;
                edges.insert({id(i, j), id(ii, jj)});
            }
        }
    }

    start = id(S.first, S.second);

    for (auto &[a, b]: edges) {
        if (edges.count(mp(b, a))) {
            adj[a].pb(b);
        }
    }

    string opt = "|-LJ7F";
    int out = 0;
    for (char &c: opt) {
        vpi dir = connect(c);
        for (auto &[a, b]: dir) {
            int ii = S.first + a;
            int jj = S.second + b;
            if (ii < 0 || jj < 0 || ii >= n || jj >= m) continue;
            int nxt = id(ii, jj);
            if (edges.count(mp(nxt, start))) {
                adj[start].pb(nxt);
                adj[nxt].pb(start);
            }
        }

        if (!loop(adj)) {
            rep(i, 0, n * m) {
                if (sz(adj[i]) && adj[i].back() == start) {
                    adj[i].pop_back();
                }
            } 
            adj[start].clear();
            continue;
        }
        vi dis = bfs(adj);      
        rep(i, 0, n * m) {
            if (dis[i] == INT_MAX) continue;
            out = max(dis[i], out);
        }
    }

    cout << out << endl;
    return 0;
}

int main() {
    solve();
    return 0;
}
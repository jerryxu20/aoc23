#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<pi> vpi;
typedef vector<string> vs;
typedef vector<vi> vii;

#define rep(i, a, b) for (int i=a; i<(b); i++)
#define trav(x,A) for (auto& x : A)

#define sz(x) (int)(x).size()
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back

int n, m;
vii seen;
vs grid;

vpi delta = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

bool match(char c, int a, int b) {
    if (c == '#') return false;
    return true;
}

int dfs(int i, int j) {
    if (i == n - 1) return 1;

    seen[i][j] = 1;
    int ans = 0;
    for (auto &[a, b]: delta) {
        int ii = i + a;
        int jj = j + b;
        if (ii < 0 || jj < 0 || ii >= n || jj >= m) continue;
        if (!match(grid[ii][jj], a, b)) continue;
        if (seen[ii][jj]) continue;
        ans = max(ans, dfs(ii, jj));
    }
    seen[i][j] = 0;

    if (ans == 0) return 0;
    return ans + 1;
    
}

int solve() {
    string s;
    while(cin >> s) {
        grid.pb(s);
    }

    n = sz(grid);
    m = sz(grid[0]);

    seen.resize(n, vi(m));
    rep(j, 0, m) {
        if (grid[0][j] == '.') {
            cout << dfs(0, j) - 1 << endl;
            break;
        }
    }
    return 0;
}

int main() {
    solve();
    return 0;
}
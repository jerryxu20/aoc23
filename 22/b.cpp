#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pi;

typedef vector<int> vi;
typedef vector<vi> vii;


#define rep(i, a, b) for (int i=a; i<(b); i++)
#define trav(x,A) for (auto& x : A)

#define sz(x) (int)(x).size()
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back


int solve() {
    int x1, y1, z1, x2, y2, z2;
    vector<pair<vi, vi>> bricks;
    char c;
    int x, y, z;
    x = y = z = 0;
    while(cin >> x1 >> c >> y1 >> c >> z1 >> c >> x2 >> c >> y2 >> c >> z2) {
        bricks.pb({{x1, y1, z1}, {x2, y2, z2}});
        assert(z1 <= z2);
        assert(x1 <= x2);
        assert(y1 <= y2);
        x = max({x, x1, x2});
        y = max({y, y1, y2});
        z = max({z, z1, z2});
    }

    sort(all(bricks), [] (auto &a, auto &b) {
        return a.first[2] < b.first[2];
    });

    vii adj(sz(bricks)), t_adj(sz(bricks));

    vii level(x + 1, vi(y + 1, -1));
    vector<int> resting(sz(bricks), 1);

    int idx = 0; 
    vector<pi> nodes;
    for (auto &[a, b]: bricks) {
        int rest = 1;
        map<int, set<int>> cnt;
        for (int i = a[0]; i <= b[0]; i++) {
            for (int j = a[1]; j <= b[1]; j++) {
                if (level[i][j] == -1) continue;
                rest = max(rest, resting[level[i][j]] + 1);
                cnt[resting[level[i][j]]].insert(level[i][j]);
            }
        }

        for (auto node: cnt[rest - 1]) {
            t_adj[idx].pb(node);
            adj[node].pb(idx);
        }


        for (int i = a[0]; i <= b[0]; i++) {
            for (int j = a[1]; j <= b[1]; j++) {
                level[i][j] = idx;
            }
        }
        resting[idx] = rest + (b[2] - a[2]);
        nodes.pb({resting[idx], idx});
        idx++;
    }

    sort(all(nodes), greater<pi>());
    vi dp(sz(bricks));

    ll ans = 0;
    rep(i, 0, sz(nodes)) {
        auto [_, node] = nodes[i];
        set<int> fallen;
        fallen.insert(node);
        vi cnt(sz(bricks));
        queue<int> q;
        q.push(node);

        while(sz(q)) {
            auto bad = q.front();
            q.pop();

            trav(nxt, adj[bad]) {
                cnt[nxt]++;
                if (cnt[nxt] == sz(t_adj[nxt]) && !fallen.count(nxt)) {
                    q.push(nxt);
                    fallen.insert(nxt);
                }
            }
        }
        ans += sz(fallen) - 1;
        
    }
    cout << ans << endl;
    return 0;
}

int main() {
    solve();
    return 0;
}
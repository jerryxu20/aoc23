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

    vii level(x + 1, vi(y + 1, -1));

    vector<int> resting(sz(bricks), 1);

    set<int> allowed;
    rep(i, 0, sz(bricks)) {
        allowed.insert(i);
    }

    int idx = 0;
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

        if (sz(cnt[rest - 1]) == 1) {
            for (auto node: cnt[rest - 1]) {
                allowed.erase(node);
            }
        }


        for (int i = a[0]; i <= b[0]; i++) {
            for (int j = a[1]; j <= b[1]; j++) {
                level[i][j] = idx;
            }
        }

        resting[idx] = rest + (b[2] - a[2]);
        idx++;
    }
    cout << sz(allowed) << endl;
    return 0;
}

int main() {
    solve();
    return 0;
}
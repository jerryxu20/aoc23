#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<vi> vii;

#define rep(i, a, b) for (int i=a; i<(b); i++)
#define trav(x,A) for (auto& x : A)

#define sz(x) (int)(x).size()
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back


const int MOD = 1000000007;
const char nl = '\n';


map<string, int> ID;
vii adj;
int N = 0;
int id(string &s) {
    if (ID.count(s)) return ID[s];
    ID[s] = N++;
    adj.pb({});
    return ID[s];
}

struct Dinic {
	struct Edge {
		int to, rev;
		ll c, oc;
		ll flow() { return max(oc - c, 0LL); } // if you need flows
	};
	vi lvl, ptr, q;
	vector<vector<Edge>> adj;
	Dinic(int n) : lvl(n), ptr(n), q(n), adj(n) {}
	void addEdge(int a, int b, ll c, ll rcap = 0) {
		adj[a].push_back({b, sz(adj[b]), c, c});
		adj[b].push_back({a, sz(adj[a]) - 1, rcap, rcap});
	}
	ll dfs(int v, int t, ll f) {
		if (v == t || !f) return f;
		for (int& i = ptr[v]; i < sz(adj[v]); i++) {
			Edge& e = adj[v][i];
			if (lvl[e.to] == lvl[v] + 1)
				if (ll p = dfs(e.to, t, min(f, e.c))) {
					e.c -= p, adj[e.to][e.rev].c += p;
					return p;
				}
		}
		return 0;
	}
	ll calc(int s, int t) {
		ll flow = 0; q[0] = s;
		rep(L,0,31) do { // 'int L=30' maybe faster for random data
			lvl = ptr = vi(sz(q));
			int qi = 0, qe = lvl[s] = 1;
			while (qi < qe && !lvl[t]) {
				int v = q[qi++];
				for (Edge e : adj[v])
					if (!lvl[e.to] && e.c >> (30 - L))
						q[qe++] = e.to, lvl[e.to] = lvl[v] + 1;
			}
			while (ll p = dfs(s, t, LLONG_MAX)) flow += p;
		} while (lvl[t]);
		return flow;
	}
	bool leftOfMinCut(int a) { return lvl[a] != 0; }
};

vs parse(string s) {
    vector<string> parts;
    string cur = "";
    s += ' ';
    trav(c, s) {
        if (c == ' ') {
            if (sz(cur)) parts.pb(cur);
            cur = "";
            continue;
        }
        cur.pb(c);
    }
    return parts;
}

int solve(int tt) {
    string a, b;
    char c;
    while(cin >> a) {
        a.pop_back();
        int u = id(a);
        getline(cin, b);
        vs nxt = parse(b);
        trav(s, nxt) {
            int v = id(s);
            adj[u].pb(v);
            adj[v].pb(u);
        }
    }

    Dinic flow(N);
    rep(i, 0, N) {
        trav(nxt, adj[i]) {
            flow.addEdge(i, nxt, 1);
        }
    }

    rep(i, 0, N) {
        rep(j, 0, i) {
            Dinic f = flow;
            if (f.calc(i, j) == 3) {
                ll left = 0;
                ll right = 0;
                rep(i, 0, N) {
                    if (f.leftOfMinCut(i)) left++;
                    else right++;
                }
                cout << left << " " << right << endl;
                cout << left * right << endl;
                return 0;
   
            } 
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
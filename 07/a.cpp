#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;

#define rep(i, a, b) for (int i=a; i<(b); i++)

#define sz(x) (int)(x).size()
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back

vi freq(string &s) {
    map<char, int> cnt;
    for (char &c: s) {
        cnt[c]++;
    }
    vector<int> rank;
    for (auto &[a, b]: cnt) {
        rank.pb(b);
    }
    sort(all(rank));
    return rank;
}

int rrank(vi &a) {
    if (a.back() == 5) return 0;
    if (a.back() == 4) return 1;
    if (a.back() == 3 && sz(a) == 2) return 2;
    if (a.back() == 3) return 3;
    if (a.back() == 2 && sz(a) == 3) return 4;
    if (a.back() == 2) return 5;
    return 6;
}

string order = "AKQJT98765432";


bool comp(string &a, string &b) {
    vi A = freq(a);
    vi B = freq(b);
    if (rrank(A) != rrank(B)) return rrank(A) < rrank(B);

    rep(i,0, sz(a))  {
        int aa = find(all(order), a[i]) - order.begin();
        int bb = find(all(order), b[i]) - order.begin();
        if (aa != bb) return aa < bb;
    }
    return true;
}


int solve() {
    string hand;
    ll amount;
    vector<pair<string, ll>> cards;
    while(cin >> hand >> amount) {
        cards.push_back(mp(hand, amount));
    }

    sort(all(cards), [&] (auto &a, auto &b) {
        return comp(a.first, b.first);
    });

    reverse(all(cards));
    ll ans = 0;
    rep(i, 0, sz(cards)) {
        ans += (i + 1) * cards[i].second;
    }
    cout << ans << endl;
    return 0;
}

int main() {
    solve();
}
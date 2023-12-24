#include <bits/stdc++.h>
using namespace std;


typedef long long ll;
typedef long double ld;
typedef pair<int, int> pi;
typedef vector<int> vi;
typedef tuple<int,int,int> ti;
typedef vector<vi> vii;

#define rep(i, a, b) for (int i=a; i<(b); i++)
#define trav(x,A) for (auto& x : A)

#define sz(x) (int)(x).size()
#define all(x) x.begin(), x.end()
#define mp make_pair
#define pb push_back

const ll mn = 200000000000000;
const ll mx = 400000000000000;


template <class T> int sgn(T x) { return (x > 0) - (x < 0); }
template<class T>
struct Point {
	typedef Point P;
	T x, y;
	explicit Point(T x=0, T y=0) : x(x), y(y) {}
	bool operator<(P p) const { return tie(x,y) < tie(p.x,p.y); }
	bool operator==(P p) const { return tie(x,y)==tie(p.x,p.y); }
	P operator+(P p) const { return P(x+p.x, y+p.y); }
	P operator-(P p) const { return P(x-p.x, y-p.y); }
	P operator*(T d) const { return P(x*d, y*d); }
	P operator/(T d) const { return P(x/d, y/d); }
	T dot(P p) const { return x*p.x + y*p.y; }
	T cross(P p) const { return x*p.y - y*p.x; }
	T cross(P a, P b) const { return (a-*this).cross(b-*this); }
	T dist2() const { return x*x + y*y; }
	double dist() const { return sqrt((double)dist2()); }
	// angle to x-axis in interval [-pi, pi]
	double angle() const { return atan2(y, x); }
	P unit() const { return *this/dist(); } // makes dist()=1
	P perp() const { return P(-y, x); } // rotates +90 degrees
	P normal() const { return perp().unit(); }
	// returns point rotated 'a' radians ccw around the origin
	P rotate(double a) const {
		return P(x*cos(a)-y*sin(a),x*sin(a)+y*cos(a)); }
	friend ostream& operator<<(ostream& os, P p) {
		return os << "(" << p.x << "," << p.y << ")"; }
};

template<class P>
pair<int, P> lineInter(P s1, P e1, P s2, P e2) {
	auto d = (e1 - s1).cross(e2 - s2);
	if (d == 0) // if parallel
		return {-(s1.cross(e1, s2) == 0), P(0, 0)};
	auto p = s2.cross(e1, e2), q = s2.cross(e2, s1);
	return {1, (s1 * p + e1 * q) / d};
}

int solve() {
    typedef Point<long double> P;
    vector<pair<P, P>> pts;
    ll x, y, z, vx, vy, vz;
    char c;

    while(cin >> x >> c >> y >> c >> z >> c >> vx >> c >> vy >> c >> vz) {
        pts.pb({P(x, y), P(vx, vy)});
    }

    int ans = 0;
    rep(i, 0, sz(pts)) {
        rep(j, 0, i) {
            auto [a, p]= lineInter(pts[i].first, pts[i].first + pts[i].second, pts[j].first, pts[j].first + pts[j].second);
            if (a != 1) continue;

            ld mxx = mx;
            ld mxy = mx;
            ld mnx = mn;
            ld mny = mn;
            if (pts[i].second.x < 0) mxx = min(mxx, pts[i].first.x);
            if (pts[i].second.x > 0) mnx = max(mnx, pts[i].first.x);
            
            if (pts[j].second.x < 0) mxx = min(mxx, pts[j].first.x);
            if (pts[j].second.x > 0) mnx = max(mnx, pts[j].first.x);

            if (pts[i].second.y < 0) mxy = min(mxy, pts[i].first.y);
            if (pts[i].second.y > 0) mny = max(mny, pts[i].first.y);

            if (pts[j].second.y < 0) mxy = min(mxy, pts[j].first.y);
            if (pts[j].second.y > 0) mny = max(mny, pts[j].first.y);
            if (p.x < mnx || p.x > mxx || p.y < mny || p.y > mxy) continue;
            ans++;
        }
    }
    cout << ans << endl;
    return 0;
}

int main() {
	solve();
    return 0;
}
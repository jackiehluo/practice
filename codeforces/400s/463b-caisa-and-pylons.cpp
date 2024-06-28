#include <bits/stdc++.h>
using namespace std;
#define ll long long

int main () {
    ll n;  cin >> n;
    vector<ll> h(n+1, 0);
    ll energy = 0, pay = 0;
    for (ll i = 1; i <= n; ++i) {
        cin >> h[i];
        energy += h[i-1]-h[i];
        if (energy < 0) {
            pay -= energy;
            energy = 0;
        }
    }
    cout << pay << endl;
    return 0;
}

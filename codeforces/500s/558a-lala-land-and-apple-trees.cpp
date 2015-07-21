#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int n, s(0);
    cin >> n;
    vector<pair<int,int>> t(n);

    for (int i = 0; i < n; i++) cin >> t[i].first >> t[i].second;

    sort(t.begin(), t.end());
    int z = upper_bound(t.begin(), t.end(), make_pair(0, 0)) - t.begin();

    if (z > n / 2) for (int i = 2 * z - n - 1; i < n; i++) s += t[i].second;
    else for (int i = 0; i < min(2 * z + 1, n); i++) s += t[i].second;

    cout << s << endl;
    return 0;
}
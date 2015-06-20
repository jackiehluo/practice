#include <iostream>
#include <algorithm>
#include <utility>
#include <vector>
using namespace std;

int main()
{
    int n, k, t;
    cin >> n >> k;
    pair<int, int> c;
    vector<pair<int, int>> d;

    for (int i = 1; i <= n; i++)
    {
        cin >> t;
        c = make_pair(t, i);
        d.push_back(c);
    }

    sort(d.begin(), d.end());
    int count = 0, sum = 0;

    for (auto p: d)
    {
        sum += p.first;
        if (sum > k)
            break;
        count++;
    }

    cout << count << endl;

    for (int i = 0; i < count; i++)
        cout << d[i].second << " ";

    return 0;
}
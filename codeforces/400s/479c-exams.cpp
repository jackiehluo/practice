#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, d(-1);
    cin >> n;
    pair<int, int> a[n];

    for (int i = 0; i < n; i++)
        cin >> a[i].first >> a[i].second;

    sort(a, a + n);

    for (int i = 0; i < n; i++)
        if(a[i].second >= d)
            d = a[i].second;
        else
            d = a[i].first;

    cout << d << endl;
    return 0;
}
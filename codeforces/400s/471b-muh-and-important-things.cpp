#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, c(0);
    cin >> n;
    pair<int, int> a[2005];
    for (int i = 0; cin >> a[i].first; i++) a[i].second = i;
    sort(a, a + n);
    
    for (int i = 0; i + 1 < n; i++)
    {
        if (a[i].first == a[i + 1].first) c++;
        if (c == 2)
        {
            cout << "YES" << endl;
            for (int j = 0; j < n; j++) cout << a[j].second + 1 << " ";
            cout << endl;
            c = 0;
            for (int j = 0; j + 1 < n; j++)
            {
                if (a[j].first == a[j + 1].first)
                {
                    c++;
                    swap(a[j].second, a[j + 1].second);
                    for (int k = 0; k < n; k++) cout << a[k].second + 1 << " ";
                    cout << endl;
                    swap(a[j].second, a[j + 1].second);
                }
                if (c == 2) return 0;
            }
        }
    }

    cout << "NO" << endl;
    return 0;
}

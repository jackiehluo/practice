#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n, t, r(0);
    cin >> n;
    map <int, int> c;
    for (;cin >> t;)
        if (t > 0)
        {
            c[t]++;
            if (c[t] == 2) r++;
            else if (c[t] > 2)
            {
                cout << -1 << endl;
                return 0;
            }
        }
    cout << r << endl;
    return 0;
}

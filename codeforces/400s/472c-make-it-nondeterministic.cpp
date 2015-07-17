#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<string> x(n), y(n);
    for(int i = 0; i < n; i++) cin >> x[i] >> y[i];
    string p;
    for (int i; cin >> i;)
    {
        i--;
        if (min(x[i], y[i]) > p) p = min(x[i], y[i]);
        else if (x[i] > p) p = x[i];
        else if (y[i] > p) p = y[i];
        else
        {
            cout << "NO" << endl;
            return 0;
        }
    }
    cout << "YES" << endl;
    return 0;
}

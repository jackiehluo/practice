#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n, r(0);
    cin >> n;
    map<string, int> v;
    string s;
    for (int i = 0; cin >> s; i++)
    {
        v[s]++;
        r = max(r, v[s]);
    }
    cout << r << endl;
    return 0;
}

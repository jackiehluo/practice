#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, r(0), m(0);
    cin >> n;
    vector<int> v(n);
    for (int i = 0; cin >> v[i]; i++);
    for (int i = 0; i < v.size(); i++)
        if (v[i] == i) r++;
        else if (v[v[i]] == i) m = 2;
        else m = max(m, 1);
    cout << r + m << endl;
    return 0;
}

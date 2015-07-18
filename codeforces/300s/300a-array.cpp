#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, t;
    cin >> n;
    vector<int> a, b, c;

    for (int t; cin >> t;)
        if (t < 0) a.push_back(t);
        else if (t == 0) b.push_back(t);
        else c.push_back(t);

    cout << 1 << " " << a[0] << endl;
    if (c.size() == 0)
    {
        cout << 2 << " " << a[1] << " " << a[2] << endl;
        a.erase(a.begin(), a.begin() + 3);
    }
    else
    {
        cout << 1 << " " << c[0] << endl;
        a.erase(a.begin()), c.erase(c.begin());
    }
    cout << a.size() + b.size() + c.size() << " ";
    for (int i = 0; i < a.size(); i++) cout << a[i] << " ";
    for (int i = 0; i < b.size(); i++) cout << b[i] << " ";
    for (int i = 0; i < c.size(); i++) cout << c[i] << " ";
    return 0;
}
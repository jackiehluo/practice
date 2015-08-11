#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main()
{
    int n, t, m(0), s(0);
    cin >> n;
    char c;
    vector<int> q, r;
    set<int> p;
    for (;cin >> c >> t;)
        if (c == '+')
        {
            q.push_back(t);
            p.insert(t);
        }
        else
        {
            q.push_back(-t);
            if (!p.count(t)) r.push_back(t);
            else p.erase(t);
        }
    for (auto it : r)
    {
        if (it > 0) s++;
        else s--;
        m = max(m, s);
    }
    for (auto it: q)
    {
        if (it > 0) s++;
        else s--;
        m = max(m, s);
    }
    cout << m << endl;
    return 0;
}
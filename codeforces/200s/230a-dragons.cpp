#include <iostream>
#include <map>
using namespace std;

int main()
{
    int s, n, x, y;
    map<int, int> d;
    bool alive = true;
    cin >> s >> n;

    for(int i = 0; i < n; i++)
    {
        cin >> x >> y;
        if(d.find(x) == d.end())
            d[x] = y;
        else
            d[x] += y;
    }

    for(map<int, int>::iterator it = d.begin(); it != d.end(); ++it)
    {
        if(it->first < s)
            s += it->second;
        else
        {
            alive = false;
            break;
        }
    }

    if(alive == true)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}
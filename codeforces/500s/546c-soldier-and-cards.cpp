#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int n, t, c, k1, k2, f, s;
    queue<int> first, second;
    cin >> n >> k1;
    for (int i = 0; i < k1; i++)
    {
        cin >> t;
        first.push(t);
    }
    cin >> k2;
    for (int i = 0; i < k2; i++)
    {
        cin >> t;
        second.push(t);
    }
    while (c < 100000 and first.size() and second.size())
    {
        f = first.front();
        first.pop();
        s = second.front();
        second.pop();
        if (f > s)
        {
            first.push(s);
            first.push(f);
        }
        else
        {
            second.push(f);
            second.push(s);
        }
        c++;
    }
    if (second.empty()) cout << c << " 1" << endl;
    else if (first.empty()) cout << c << " 2" << endl;
    else cout << -1 << endl;
    return 0;
}

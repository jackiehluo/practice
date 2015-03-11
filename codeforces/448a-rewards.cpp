#include <iostream>
using namespace std;

int main()
{
    int a, b, n, s;
    int t = 0, m = 0;

    for(int i = 0; i < 3; i++)
    {
        cin >> a;
        t += a;
    }

    for(int j = 0; j < 3; j++)
    {
        cin >> b;
        m += b;
    }

    cin >> n;
    s = (t / 5) + (m / 10);
    if(t % 5 != 0)
        s++;
    if(m % 10 != 0)
        s++;

    if(s <= n)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}

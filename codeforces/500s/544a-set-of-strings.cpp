#include <iostream>
#include <string>
using namespace std;

int main()
{
    int k, n(0), c[256] = {0};
    string q;
    cin >> k >> q;
    for (int i = 0; i < q.length(); i++) c[q[i]]++;
    for (int i = 0; i < 256; i++) n += c[i] != 0, c[i] = 0;
    if (n < k)
    {
        cout << "NO" << endl;
        return 0;
    }
    cout << "YES";
    for (int i = 0; i < q.length(); i++)
    {
        if (!c[q[i]] and k)
        {
            k--, c[q[i]]++;
            cout << endl;
        }
        cout << q[i];
    }
    return 0;
}

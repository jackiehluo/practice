#include <iostream>
using namespace std;

int prime(int x)
{
    for (int i = 2; i * i <= x; i++)
        if (x % i == 0) return false;
    return true;
}

int main()
{
    int n, m;
    cin >> n >> m;
    if (!prime(m))
    {
        cout << "NO" << endl;
        return 0;
    }
    for (int i = n + 1; i <= 10000; i++)
        if (prime(i))
        {
            cout << (i == m ? "YES" : "NO") << endl;
            return 0;
        }
}

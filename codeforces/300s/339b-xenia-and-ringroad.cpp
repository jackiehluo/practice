#include <iostream>
using namespace std;

int main()
{
    long long n, m;
    cin >> n >> m;
    long long a[m];
    long long t = 0;

    for(long long i = 0; i < m; i++)
    {
        cin >> a[i];
        if(i > 0)
        {
            if(a[i] < a[i - 1])
                t += n - a[i - 1] + a[i];
            else
                t += a[i] - a[i - 1];
        }
        else
            t += a[i] - 1;
    }

    cout << t << endl;
    return 0;
}

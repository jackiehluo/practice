#include <iostream>
using namespace std;

int main()
{
    int n, p, q, t;
    cin >> n;
    int a[n];
    int max = 0;
    int min = 100;

    for(int i = 0; i < n; i++)
    {
        cin >> a[i];
        if(a[i] > max)
        {
            max = a[i];
            p = i;
        }
        if(a[i] <= min)
        {
            min = a[i];
            q = i;
        }
    }

    t = p + (n - 1 - q);
    if(p > q)
        t--;

    cout << t << endl;
    return 0;
}

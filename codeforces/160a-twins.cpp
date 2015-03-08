#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int *v = new int[n];
    int c = 0, s = 0, t = 0;

    for(int i = 0; i < n; i++)
    {
        cin >> v[i];
        t += v[i];
    }

    sort(v, v + n);

    while(s <= t / 2)
    {
        c++;
        s += v[n - c];
    }
    
    cout << c << endl;
    return 0;
}

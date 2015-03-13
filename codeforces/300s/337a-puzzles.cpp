#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    int n, m, d;
    cin >> n >> m;
    int p[m];
    int s = 1000;

    for(int i = 0; i < m; i++)
        cin >> p[i];
    
    sort(p, p + m);
    
    if(m == n)
        s = p[m - 1] - p[0];
    else
        for(int j = 0; j < m - n + 1; j++)
        {
            d = 0;
            for(int k = 0; k < n - 1; k++)
                d += p[j + k + 1] - p[j + k];
            if(d < s)
                s = d;
        }

    cout << s << endl;
    return 0;
}

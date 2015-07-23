#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int g[n];

    for(int i = 0; i < n; i++) cin >> g[i];

    sort(g, g + n);
    int i = 0;
    int t = 1;
    int j = n - 1;

    while(i != j)
    {
        if(g[i] + g[j] <= 4)
        {
            g[j] += g[i];
            i++;
        }
        else
        {
            j--;
            t++;
        }
    }
    cout << t << endl;
    return 0;
}

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int k, n;
    int sum = 0, ind = 0;
    vector<int> g;
    cin >> k;

    for(int i = 0; i < 12; i++)
    {
        cin >> n;
        g.push_back(n);
    }

    sort(g.begin(), g.end(), greater<int>());

    while(sum < k)
    {
        sum += g[ind];
        ind++;
        if(ind > 12)
        {
            ind = -1;
            break;
        }
    }

    if(k == 0)
        cout << 0 << endl;
    else
        cout << ind << endl;
    return 0;
}
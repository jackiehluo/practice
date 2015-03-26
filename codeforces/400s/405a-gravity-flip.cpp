#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    long long n, v;
    vector<long long> c;
    cin >> n;
    
    for(int i = 0; i < n; i++)
    {
        cin >> v;
        c.push_back(v);
    }

    sort(c.begin(), c.end());

    for(vector<long long>::iterator it = c.begin(); it != c.end(); ++it)
        cout << *it << " ";
    return 0;
}

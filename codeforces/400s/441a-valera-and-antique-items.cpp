#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, v, c, t;
    cin >> n >> v;
    vector<int> sellers;

    for (int i = 1; i <= n; i++)
    {
        bool d = false;
        cin >> c;
        for (int j = 0; j < c; j++)
        {
            cin >> t;
            if (!d and v > t)
            {
                sellers.push_back(i);
                d = true;
            }
        }
    }

    cout << sellers.size() << endl;

    for (auto& seller : sellers)
        cout << seller << " ";
    return 0;
}
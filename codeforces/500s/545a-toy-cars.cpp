#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, t, c(0);
    cin >> n;
    vector<int> g;

    for (int i = 1; i <= n; i++)
    {
        bool f = false;
        for (int j = 0; j < n; j++)
        {
            cin >> t;
            if (t == 1 or t == 3)
                f = true;
        }
        if (!f)
        {
            c++;
            g.push_back(i);
        }
    }

    cout << c << endl;

    for (auto& car : g)
        cout << car << " ";

    return 0;
}
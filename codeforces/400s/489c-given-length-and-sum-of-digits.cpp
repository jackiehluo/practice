#include <iostream>
using namespace std;

int main()
{
    int m, s;
    cin >> m >> s;
    string min = "1", max;

    if (s == 0 and m == 1)
        cout << "0 0" << endl;
    else if (s == 0 and m > 1)
        cout << "-1 -1" << endl;
    else
    {
        while (max.size() < m)
            max += '9';
        while (min.size() < m)
            min += '0';
        int l = min.size() - 1;
        while (s != 0 and l >= 0)
        {
            min[l]++, s--;
            if (min[l] == '9')
                l--;
        }
        if (s > 0)
            cout << "-1 -1" << endl;
        else
            cout << min << " " << max;
    }
    return 0;
}
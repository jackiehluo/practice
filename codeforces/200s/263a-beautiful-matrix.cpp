#include <algorithm>
#include <cmath>
#include <iostream>
using namespace std;

int main()
{
    int n, m;
    int p[2];

    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < 5; j++)
        {
            cin >> n;
            if(n == 1)
            {
                p[0] = i;
                p[1] = j;
                break;
            }
        }
    }

    m = abs(p[0] - 2) + abs(p[1] - 2);
    cout << m << endl;
    return 0;
}

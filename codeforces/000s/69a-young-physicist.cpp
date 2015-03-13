#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int v[n][3];
    int a = 0, b = 0, c = 0;

    for(int i = 0; i < n; i++)
    {
        cin >> v[i][0] >> v[i][1] >> v[i][2];
    }

    for(int j = 0; j < n; j++)
    {
        a += v[j][0];
        b += v[j][1];
        c += v[j][2];
    }

    if(a == 0 && b == 0 && c == 0)
        cout << "YES" << endl;
    else
        cout << "NO" << endl;
    return 0;
}

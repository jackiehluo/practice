#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int u[n][2];
    int c = 0;

    for(int i = 0; i < n; i++)
    {
        cin >> u[i][0] >> u[i][1];
    }

    for(int j = 0; j < n; j++)
    {
        for(int k = 0; k < n; k++)
        {
            if(j != k && u[j][0] == u[k][1])
                c++;
        }
    }

    cout << c << endl;
    return 0;
}

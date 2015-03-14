#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    int t[n][n];
    int m = 0;

    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(i == 0 || j == 0)
                t[i][j] = 1;
            else
                t[i][j] = t[i][j - 1] + t[i - 1][j];
            if(t[i][j] > m)
                m = t[i][j];
        }
    }
    cout << m << endl;
    return 0;     
}

#include <iostream>
using namespace std;

int main()
{
    int l, a[10][10];
    for (int i = 1; i <= 3; i++)
        for (int j = 1; j <= 3; j++)
            a[i][j] = 0;

    for (int i = 1; i <= 3; i++)
        for (int j = 1; j <= 3; j++)
        {
            cin >> l;
            a[i][j] += l;
            a[i + 1][j] += l;
            a[i - 1][j] += l;
            a[i][j + 1] += l;
            a[i][j - 1] += l;
        }

    for (int i = 1; i <= 3; i++)
    {
        for (int j = 1; j <= 3; j++)
            cout << (a[i][j] % 2 == 1 ? "0" : "1");
        cout << endl;
    }
    return 0;
}

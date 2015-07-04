#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    cout << (n * n + 1) / 2 << endl;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if ((i + j) % 2)
                cout << ".";
            else
                cout << "C";
        }
        cout << endl;
    }
    return 0;
}
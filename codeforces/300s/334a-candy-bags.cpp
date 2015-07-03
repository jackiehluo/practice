#include <iostream>
using namespace std;

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        cout << i + 1 << " ";
        for (int j = 1; j < n; j++)
            cout << n * j + (i + j) % n + 1 << endl;
    }

    return 0;
}

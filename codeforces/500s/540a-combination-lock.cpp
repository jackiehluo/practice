#include <iostream>
#include <sstream>
#include <stdlib.h>
using namespace std;

int main()
{
    int n;
    string a, b;
    cin >> n >> a >> b;
    int count;

    for (int i = 0; i < n; i++)
    {
        if (a[i] - b[i] != 0)
        {
            if (abs(a[i] - b[i]) <= 10 - abs(a[i] - b[i]))
                count += abs(a[i] - b[i]) - '0';
            else
                count += 10 - abs(a[i] - b[i]) - '0';
        }
    }

    cout << count << endl;
    return 0;
}
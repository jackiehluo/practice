#include <iostream>
using namespace std;

int main()
{
    int n, a, b;
    cin >> n;
    bool h = false;

    for (int i = 0; i < n; i++)
    {
        cin >> a >> b;
        if (a != b)
        {
            h = true;
            break;
        }
    }

    if (h)
        cout << "Happy Alex" << endl;
    else
        cout << "Poor Alex" << endl;
    return 0;
}
#include <iostream>
using namespace std;

int main()
{
    int n, k, t;
    cin >> n >> k;
    int count = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> t;
        if (t + k <= 5)
            count++;
    }

    cout << count / 3 << endl;
    return 0;
}

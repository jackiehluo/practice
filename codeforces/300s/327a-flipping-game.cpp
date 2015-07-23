#include <iostream>
using namespace std;

int main()
{
    int n, t;
    int count = 0, extra = 0, max_extra = -1;
    cin >> n;

    while (n--)
    {
        cin >> t;
        if (t == 1)
        {
            count++;
            if (extra > 0)
                extra--;
        }
        else
        {
            extra++;
            if (extra > max_extra)
                max_extra = extra;
        }
    }
    cout << count + max_extra << endl;
    return 0;
}

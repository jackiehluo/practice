#include <iostream>
using namespace std;

int main()
{
    double t, n;
    cin >> t;

    for(int i = 0; i < t; i++)
    {
        cin >> n;
        bool p = false;
        for(int j = 1; j <= 360; j++)
        {
            if(n == (180 * (j - 2)) / double(j))
            {
                p = true;
                break;
            }
            else if(n < (180 * (j - 2)) / j)
            {
                break;
            }
        }
        if(p == true)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }
    
    return 0;
}
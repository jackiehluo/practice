#include <iostream>
using namespace std;

int main()
{
    int n, x;
    cin >> n;
    int d = 0;
    int r = 0;
    int s = n * 2;
    bool mid = false;

    while(r <= n * 2 + 1)
    {
        if(r == n)
            mid = true;
        for(int i = 0; i < s; i++)
            cout << " ";
        x = 0;
        for(int j = 0; j < d * 2 + 1; j++)
        {
            cout << x;
            if(j < d)
                x++;
            else
                x--;
            if(j != d * 2)
                cout << " ";
            else
                cout << endl;
        }
        if(mid == false)
        {
            d++;
            s -= 2;
        }
        else
        {
            d--;
            s += 2;
        }
        r++;
    }
    return 0;
}

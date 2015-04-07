#include <iostream>
using namespace std;

int main()
{
    int n;
    int x = 1;
    bool mid = false;
    cin >> n;

    for(int i = 0; i < n; i++)
    {
        if(i == (n - 1) / 2)
            mid = true;
        string a = string((n - x) / 2, '*');
        string d = string(x, 'D');
        cout << a << d << a << endl;
        if(mid == true)
            x -= 2;
        else
            x += 2;
    }

    return 0;
}
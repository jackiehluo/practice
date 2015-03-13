#include <algorithm>
#include <iostream>
using namespace std;

int main()
{
    int h[4];
    int c = 0;

    for(int i = 0; i < 4; i++)
    {
        cin >> h[i];
    }

    sort(h, h + 4);

    for(int j = 0; j < 3; j++)
    {
        if(h[j] == h[j + 1])
        c++;
    }

    cout << c << endl;
    return 0;
}

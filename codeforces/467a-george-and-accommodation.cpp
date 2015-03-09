#include <iostream>
using namespace std;

int main()
{
    int n, p, q;
    cin >> n;
    int c = 0;

    for(int i = 0; i < n; i++)
    {
        cin >> p >> q;
        if(q - p >= 2)
            c++;
    }

    cout << c << endl;
    return 0;
}

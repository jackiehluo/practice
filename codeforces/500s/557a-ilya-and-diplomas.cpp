#include <iostream>
using namespace std;

int main()
{
    int n, min1, max1, min2, max2, min3, max3;
    cin >> n >> min1 >> max1 >> min2 >> max2 >> min3 >> max3;
    int a(min1), b(min2), c(min3), t(min1 + min2 + min3);

    while (t < n)
    {
        if (a < max1)
            a++;
        else if (b < max2)
            b++;
        else if (c < max3)
            c++;
        t++;
    }

    cout << a << " " << b << " " << c << endl;
    return 0;
}

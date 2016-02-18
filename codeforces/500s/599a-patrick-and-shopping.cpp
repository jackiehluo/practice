#include <iostream>
using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;
    cout << min(a + a + b + b, min(a + b + c, min(a + a + c + c, b + b + c + c))) << endl;
    return 0;
}

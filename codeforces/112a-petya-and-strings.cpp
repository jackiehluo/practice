#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string a, b, c, d;
    cin >> a >> b;
    transform(a.begin(), a.end(), a.begin(), ::tolower);
    transform(b.begin(), b.end(), b.begin(), ::tolower);
    if(string(a) > b)
        cout << 1 << endl;
    else if(string(b) > a)
        cout << -1 << endl;
    else
        cout << 0 << endl;
    return 0;
}

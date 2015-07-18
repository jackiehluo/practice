#include <iostream>
using namespace std;

int main()
{
    string s;
    cin >> s;
    int p(0);
    for (char c; cin >> c;) if (s[p] == c) p++;
    cout << p + 1 << endl;
    return 0;
}
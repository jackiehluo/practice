#include <iostream>
#include <string.h>
using namespace std;

int main()
{
    char s[100005], *p;
    cin >> s;
    if ((p = strstr(s, "AB")) and strstr(p + 2, "BA")) cout << "YES" << endl;
    else if ((p = strstr(s, "BA")) and strstr(p + 2, "AB")) cout << "YES" << endl;
    else cout << "NO" << endl;
    return 0;
}

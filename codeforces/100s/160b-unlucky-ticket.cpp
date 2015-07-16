#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n, g(0), l(0);
    cin >> n;
    char s[n * 2];
    cin >> s;

    sort(s, s + n);
    sort (s + n, s + n * 2);

    for (int i = 0; i < n; i++)
        if (s[i] > s[i + n]) g++;
        else if (s[i] < s[i + n]) l++;

    cout << ((g == n or l == n) ? "YES" : "NO") << endl;
    return 0;
}

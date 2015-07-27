#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

bool array(string a, string b)
{
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    return a == b;
}

bool automaton(string a, string b)
{
    int n = 0;
    for (int i = 0; i < a.length() and n < b.length(); i++) n += a[i] == b[n];
    return n == b.length();
}

bool both(string a, string b)
{
    for (int i = 0; i < b.length(); i++)
    {
        int p = a.find(b[i]);
        if (p == -1) return false;
        a[p] = '0';
    }
    return true;
}

int main()
{
    string a, b;
    cin >> a >> b;
    if (array(a, b)) cout << "array" << endl;
    else if (automaton(a, b)) cout << "automaton" << endl;
    else if (both(a, b)) cout << "both" << endl;
    else cout << "need tree" << endl;
    return 0;
}

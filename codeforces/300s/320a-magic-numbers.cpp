#include <iostream>
using namespace std;

int main()
{
    string n;
    cin >> n;
    int c(0);
    bool magic = true;

    for (int i = 0; i < n.length(); i++)
        if (c > 0 and c < 3 and n[i] == '4')
            c++;
        else if (n[i] == '1')
            c = 1;
        else
            magic = false;

    cout << (magic ? "YES" : "NO") << endl;
    return 0;
}

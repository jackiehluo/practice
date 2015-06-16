#include <cstdlib>
#include <iostream>
using namespace std;

int main()
{
    int x, y, steps;
    cin >> x >> y >> steps;
    int shortest = abs(x) + abs(y);

    if (shortest > steps or shortest % 2 != steps % 2)
        cout << "No" << endl;
    else
        cout << "Yes" << endl;
    return 0;
}

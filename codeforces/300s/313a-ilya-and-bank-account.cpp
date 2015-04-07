#include <algorithm>
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main()
{
    int n;
    cin >> n;
    
    stringstream ss;
    ss << n;
    string v = ss.str();

    int a = v[v.length() - 1];
    int b = v[v.length() - 2];

    if(a > b)
        v.erase(v.begin() + (v.length() - 1));
    else
        v.erase(v.begin() + (v.length() - 2));
    
    int r;
    istringstream convert(v);
    convert >> r;
    
    if(n >= 0)
        cout << n << endl;
    else
        cout << r << endl;
    return 0;
}
#include <algorithm>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main()
{
    int n;
    vector<int> s;
    map<int, int> c;
    int ones = 0, twos = 0, threes = 0;

    for(int i = 0; i < 6; i++)
    {
        cin >> n;
        s.push_back(n);
    }

    sort(s.begin(), s.end());

    for(vector<int>::iterator it1 = s.begin(); it1 != s.end(); ++it1)
    {
        if(c.find(*it1) == c.end())
            c[*it1] = 1;
        else
            c[*it1] += 1;
    }

    for(map<int, int>::iterator it2 = c.begin(); it2 != c.end(); ++it2)
    {
        if(it2->second == 1)
            ones++;
        else if(it2->second == 2)
            twos++;
        else if(it2->second == 3)
            threes++;
    }

    if(ones == 0 && twos <= 1 && threes == 0)
        cout << "Elephant" << endl;
    else if((ones == 1 || ones == 2) && twos == 0)
        cout << "Bear" << endl;
    else
        cout << "Alien" << endl;
    return 0;
}

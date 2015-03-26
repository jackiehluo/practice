#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

int main()
{
    long long n;
    string t;
    int max = 0;
    vector<string> c;
    map<string, int> counts;
    cin >> n;
    
    for(int i = 0; i <= n; i++)
    {
        getline(cin, t);
        c.push_back(t);
    }

    for(vector<string>::iterator it1 = c.begin(); it1 != c.end(); ++it1)
    {
        if(counts.find(*it1) == counts.end())
            counts[*it1] = 1;
        else
            counts[*it1] += 1;
    }

    for(map<string, int>::iterator it2 = counts.begin(); it2 != counts.end(); ++it2)
    {
        if(it2->second > max)
            max = it2->second;
    }
    
    cout << max << endl;
    return 0;
}

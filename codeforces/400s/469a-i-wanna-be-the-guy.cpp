#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main()
{
    int n, p, q, l;
    vector<int> levels;
    set<int> numbers;
    cin >> n >> p;

    for(int i = 0; i < p; i++)
    {
        cin >> l;
        levels.push_back(l);
    }

    cin >> q;

    for(int j = 0; j < q; j++)
    {
        cin >> l;
        levels.push_back(l);
    }

    for(vector<int>::iterator it1 = levels.begin(); it1 != levels.end(); ++it1)
        if(numbers.find(*it1) == numbers.end()) numbers.insert(*it1);

    bool pass = true;

    for(int k = 1; k <= n; k++)
        if(numbers.find(k) == numbers.end()) pass = false;

    if(pass == true) cout << "I become the guy." << endl;
    else cout << "Oh, my keyboard!" << endl;
    return 0;
}

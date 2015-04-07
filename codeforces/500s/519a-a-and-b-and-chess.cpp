#include <iostream>
#include <map>
using namespace std;

int main()
{
    string s;
    int w = 0, b = 0;
    map<char, int> c;
    map<char, int> v_w = {{'Q', 9}, {'R', 5}, {'B', 3}, {'N', 3}, {'P', 1}, {'K', 0}};
    map<char, int> v_b = {{'q', 9}, {'r', 5}, {'b', 3}, {'n', 3}, {'p', 1}, {'k', 0}};

    for(int i = 0; i < 8; i++)
    {
        getline(cin, s);
        int ind = 0;
        while(s[ind])
        {
            if(isalpha(s[ind]))
                if(c.find(s[ind]) == c.end())
                    c[s[ind]] = 1;
                else
                    c[s[ind]] += 1;
            ind++;
        }
    }

    for(map<char, int>::iterator it = c.begin(); it != c.end(); ++it)
    {
        if(v_w.find(it->first) != v_w.end())
            w += v_w[it->first] * it->second;
        else
            b += v_b[it->first] * it->second;
    }

    if(w > b)
        cout << "White" << endl;
    else if(b > w)
        cout << "Black" << endl;
    else
        cout << "Draw" << endl;
    return 0;
}
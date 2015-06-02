#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int n, t;
    cin >> n;

    vector<int> p;
    vector<int> m;
    vector<int> s;

    int ind = 0, p_count = 0, m_count = 0, s_count = 0;

    for (int i = 0; i < n; i++)
    {
        ind++;
        cin >> t;
        if (t == 1)
        {
            p.push_back(ind);
            p_count++;
        }
        else if (t == 2)
        {
            m.push_back(ind);
            m_count++;
        }
        else if (t == 3)
        {
            s.push_back(ind);
            s_count++;
        }
    }

    int min;

    if (p_count <= m_count and p_count <= s_count)
        min = p_count;
    else if (m_count <= p_count and m_count <= s_count)
        min = m_count;
    else
        min = s_count;

    cout << min << endl;

    for (int i = 0; i < min; i++)
        cout << p[i] << " " << m[i] << " " << s[i] << endl;

    return 0;
}
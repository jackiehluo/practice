#include <iostream>
using namespace std;

int main()
{
	int n, t, x;
	string s;
	cin >> n >> t >> s;

	for(int i = 0; i < t; i++)
	{
		for(int j = 0; j < s.length() - 1; j++)
		{
			if(s[j] == 'B' && s[j + 1] == 'G')
			{
				x = s[j];
				s[j] = s[j + 1];
				s[j + 1] = x;
                j++;
			}
		}
	}

	cout << s << endl;
	return 0;
}

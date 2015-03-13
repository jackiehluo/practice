#include <iostream>
using namespace std;

int main()
{
	int n;
	string s;
	int x = 0;
	cin >> n;

	for(int i = 0; i < n; i++)
	{
		cin >> s;
		if (s.find('+') != std::string::npos)
		{
			x++;
		}
		else
			x--;
	}

	cout << x << endl;
	return 0;
}

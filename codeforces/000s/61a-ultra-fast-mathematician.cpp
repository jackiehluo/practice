#include <iostream>
using namespace std;

int main()
{
	string a, b;
	cin >> a >> b;
	
	for(int i = 0; i < a.length(); i++)
	{
		if(a[i] == b[i])
			a[i] = '0';
		else
			a[i] = '1';
	}
	cout << a << endl;
	return 0;
}

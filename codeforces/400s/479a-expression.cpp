#include <iostream>
using namespace std;

int main()
{
	int a, b, c, t;
	cin >> a >> b >> c;

	if(a == 1 && c == 1)
		t = a + b + c;
	else if(a == 1)
		t = (a + b) * c;
	else if(b == 1)
		if(a > c)
			t = a * (b + c);
		else
			t = (a + b) * c;
	else if(c == 1)
		t = a * (b + c);
	else
		t = a * b * c;

	cout << t << endl;
	return 0;
}
#include <iostream>
#include <ctype.h>
#include <set>
using namespace std;

int main()
{
   string s;
   set<char> l;
   getline(cin, s);

   int i = 0;
   while(s[i])
   {
        if(isalpha(s[i]))
            l.insert(s[i]);
        i++;
   }

   cout << l.size() << endl;
}

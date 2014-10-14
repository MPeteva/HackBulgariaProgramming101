# include <iostream>
# include <string>
using namespace std;

string DashInsert (unsigned int a)
{
	string str;
	
	while (a > 10)
	{		
		str = char((a % 10) + '0' ) + str;
		if ( ((a % 10) % 2 == 1) && ((a / 10 % 10) % 2 == 1) )
			str = '-' + str;
		a/=10;
	}
	str = char((a % 10) + '0' ) + str;
		
	return str;
}

int main ()
{
	unsigned int n;
	cin >> n;
	
	cout << DashInsert (n) <<endl;
}

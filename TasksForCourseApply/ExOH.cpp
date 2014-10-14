# include <iostream>
# include <string>
using namespace std;

bool ExOh (string a)
{
	int len = a.size ();
	int br = 0;
		
	for (int i = 0 ; i < len ; i++)
		a[i] == 'x' ? br++ : br--;
	
	return !br;
}

int main ()
{
	string str;
	cin >> str;	
		
	if (ExOh (str))
		cout<<"True"<<endl;
	else
		cout<<"False"<<endl;
}

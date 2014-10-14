# include <iostream>
# include <string>
using namespace std;

bool ABCheck (string a)
{
	int  len = a.size ();
	int  i = 0;
	bool l = 0;

	while (!l && (i < len - 4 ))
	{
		l = (( a[i] == 'a' && a[i+4] == 'b' ) || ( a[i] == 'b' && a[i+4] == 'a' ));
		i++;
	}
	
	return l;
}

int main ()
{
	string str;
	getline (cin, str);	
			
	if (ABCheck (str))
		cout<<"True"<<endl;
	else
		cout<<"False"<<endl;
}

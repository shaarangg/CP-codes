#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cin >> s;
    int l = s.length();
    int f = 0;
    for (int i = 0; i < l; i++)
    {
        if (s[i] == '0')
        {
            f = 1;
            s.erase(i, 1);
            break;
        }
    }
    if (f == 0)
    {
        s.erase(0, 1);
    }
    cout << s << endl;
    return 0;
}
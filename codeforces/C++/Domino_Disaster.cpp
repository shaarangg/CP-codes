#include <bits/stdc++.h>
using namespace std;
void solve()
{
    string s;
    int l;
    cin >> l;
    cin >> s;
    string ans = "";
    for (int i = 0; i < l; i++)
    {
        if (s[i] == 'L')
            ans += 'L';
        else if (s[i] == 'R')
            ans += 'R';
        else if (s[i] == 'U')
            ans += 'D';
        else
            ans += 'U';
    }
    cout << ans << endl;
}
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}
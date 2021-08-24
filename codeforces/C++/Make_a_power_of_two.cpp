#include <bits/stdc++.h>
using namespace std;
#define MAX pow(10, 18)
void solve(string s, vector<string> &a)
{
    int minn = pow(10, 9);
    int k, ans;
    for (auto i : a)
    { //1024
        //1052
        k = 0;
        int l = i.length();
        for (auto j : s)
        {
            if (j == i[k] && k < l)
            {
                k++;
            }
        }
        ans = (l - k) + (s.length() - k);
        minn = min(ans, minn);
    }
    cout << minn << endl;
}
int main()
{
    long long int i = 1;
    vector<string> a;
    a.push_back("1");
    while (i < MAX)
    {
        i *= 2;
        a.push_back(to_string(i));
    }
    // for (auto i : a)
    // {
    //     cout << i << " ";
    // }
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        solve(s, a);
    }
    return 0;
}
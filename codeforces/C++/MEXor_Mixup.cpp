#include <bits/stdc++.h>
using namespace std;
#define MAX 3 * 10e5
unordered_map<int, int> s;
void init()
{
    int res = 0;
    s[0] = 0;
    for (int i = 1; i < MAX; i++)
    {
        res = res ^ i;
        s[i] = res;
    }
}
void solve()
{
    int a, b;
    cin >> a >> b;
    int x = s[a - 1];
    if (x == b)
        cout << a << endl;
    else if ((x ^ b) == a)
    {
        cout << a + 2 << endl;
    }
    else
        cout << a + 1 << endl;
}
int main()
{
    int t;
    cin >> t;
    init();
    while (t--)
    {
        solve();
    }
    return 0;
}
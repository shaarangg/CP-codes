#include <bits/stdc++.h>
using namespace std;
void solve()
{
    int n, elem, count = 0, ce = -1, co = -1;
    cin >> n;
    int a[n + 1];
    a[0] = -1;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i];
    }
    while (true)
    {
        if (ce == 0 && co == 0)
        {
            cout << count - 2 << endl;
            return;
        }
        if ((count + 1) % 2 != 0)
        {
            co = 0;
            for (int i = 1; i <= n - 2; i += 2)
            {
                if (a[i] > a[i + 1])
                {
                    swap(a[i], a[i + 1]);
                    co += 1;
                }
            }
        }
        else
        {
            ce = 0;
            for (int i = 2; i <= n - 1; i += 2)
            {
                if (a[i] > a[i + 1])
                {
                    swap(a[i], a[i + 1]);
                    ce += 1;
                }
            }
        }
        count++;
    }
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
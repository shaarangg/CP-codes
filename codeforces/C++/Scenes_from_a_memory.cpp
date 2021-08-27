#include <bits/stdc++.h>
using namespace std;
bool prime[100];
void solve()
{
    int k, l;
    string n;
    cin >> k;
    cin >> n;
    int no[k];
    for (int i = 0; i < k; i++)
    {
        no[i] = n[i] - '0';
        if (no[i] == 1 || no[i] == 4 || no[i] == 6 || no[i] == 8 || no[i] == 9)
        {
            cout << 1 << endl;
            cout << no[i] << endl;
            return;
        }
    }
    for (int i = 0; i < k; i++)
    {
        for (int j = i + 1; j < k; j++)
        {
            if (!prime[no[i] * 10 + no[j]])
            {
                cout << 2 << endl;
                cout << no[i] << no[j] << endl;
                return;
            }
        }
    }
    cout << 2 << endl;
    cout << n << endl;
}
int main()
{
    int t;
    cin >> t;
    memset(prime, true, sizeof(prime));
    for (int i = 2; i < 100; i++)
    {
        if (prime[i] == true)
        {
            for (int j = i * i; j < 100; j += i)
            {
                prime[j] = false;
            }
        }
    }
    while (t--)
    {
        solve();
    }
    return 0;
}
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, count = 0;
    cin >> n;
    int prime[n + 1];
    memset(prime, 0, sizeof(prime));
    for (int i = 2; i * i < n + 1; i++)
    {
        if (!prime[i])
        {
            for (int j = i * i; j < n + 1; j += i)
            {
                prime[j] = 1;
            }
        }
    }
    while (true)
    {
        if (!prime[n])
        {
            cout << count << endl;
            break;
        }
        for (int i = 2; i < n; i++)
        {
            if (n % i == 0)
            {
                n /= i;
                count++;
                break;
            }
        }
    }
}
#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long n;
    cin >> n;
    long long arr[n];
    long long s = 0;
    for (long long i = 0; i < n; i++)
    {
        cin >> arr[i];
        s += arr[i];
    }
    if (s % 3 != 0)
        cout << 0 << endl;
    else
    {
        s /= 3;
        long long s1 = 0, s2 = 0, sum = 0, i = 0;
        while (i < n - 1)
        {
            sum += arr[i];
            i++;
            if (sum == 2 * s)
                s2 += s1;
            if (sum == s)
                s1++;
        }
        cout << s2 << endl;
    }
}
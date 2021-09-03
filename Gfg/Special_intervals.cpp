#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long n, l, r, ans, c1 = 0, c2 = 0, i, lmin = pow(-10, 9), rmax = pow(10, 9);
    cin >> n;
    vector<long long> a(n);
    vector<long long> b(n);
    unordered_map<long long, long long> d1, d2;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i] >> b[i];
    }
    // L
    sort(a.begin(), a.end());
    // R
    sort(b.begin(), b.end());
    lmin = a[0];
    rmax = b[n - 1];
    for (i = lmin; i <= rmax; i++)
    {
        if (i >= a[c1])
        {
            while (i >= a[c1])
                c1++;
        }
        if (i > b[c2])
        {
            while (i > b[c2])
                c2++;
        }
        d1[i] = n - c1;
        d2[i] = c2;
    }
    int q;
    cin >> q;
    for (int i = 0; i < q; i++)
    {
        cin >> l >> r;
        ans = n - d1[r] - d2[l];
        cout << ans << " ";
    }
    // Ans = Total special intervals — intervals ending before l — intervals starting after r.
}
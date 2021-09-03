#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, m, k, temp;
    cin >> n >> m >> k;
    vector<int> a(n);
    vector<int> elem;
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
        if (a[i] <= m)
        {
            elem.push_back(m - a[i]);
        }
        else
        {
            elem.push_back(ceil((float)a[i] / m) * m - a[i]);
        }
    }
    int count = 0, total = 0;
    sort(elem.begin(), elem.end());
    for (auto i : elem)
    {
        if (k > 0)
        {
            k -= i;
            count++;
        }
        else
        {
            break;
        }
    }
    cout << count << endl;
}
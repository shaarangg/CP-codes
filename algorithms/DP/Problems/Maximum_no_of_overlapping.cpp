#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n, elem1, elem2;
    cin >> n;
    vector<pair<int, char>> data;
    for (int i = 0; i < n; i++)
    {
        cin >> elem1 >> elem2;
        data.push_back(make_pair(elem1, 'x'));
        data.push_back(make_pair(elem2, 'y'));
    }
    sort(data.begin(), data.end());
    int count = 0, mmax = 0;
    for (auto i : data)
    {
        if (i.second == 'x')
        {
            count++;
        }
        else
        {
            count--;
        }
        mmax = max(mmax, count);
    }
    cout << mmax << endl;
}
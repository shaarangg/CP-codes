#include <bits/stdc++.h>
using namespace std;
int main()
{
    int curr = 0;
    long long int n, elem;
    unordered_map<int, int> visited;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        cin >> elem;
        elem %= 86400;
        curr += elem;
        if (curr > 86399)
        {
            curr -= 86400;
        }
        if (curr < 0)
        {
            curr = 86400 + curr;
        }
        if (visited.find(curr) == visited.end())
        {
            visited[curr] = 1;
            cout << "No" << endl;
        }
        else
        {
            cout << "Yes" << endl;
        }
    }
    return 0;
}
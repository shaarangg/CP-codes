#include <bits/stdc++.h>
using namespace std;
int main()
{
    // Range based loops
    vector<int> s;
    int size;
    cin >> size;
    int elem;
    for (int i = 0; i < size; i++)
    {
        cin >> elem;
        s.push_back(elem);
    }
    // So basically what happens value at the pointer get's copied to the value i
    for (auto i : s)
    {
        cout << i << " ";
    }
    cout << endl;
    // So now if we want to use actual values then we can do something like this
    for (auto &i : s)
    {
        i++;
        cout << i << " ";
    }
    return 0;
}
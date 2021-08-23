#include <bits/stdc++.h>
using namespace std;
int main()
{
    // Pair stores 2 values together which might be inter-connected to each other
    pair<int, int> p1;
    p1 = {2, 5};
    cout << p1.first << " " << p1.second << endl;
    // We can also store all the pairs in an array
    int a[] = {1, 2, 3};
    int b[] = {4, 5, 6};
    pair<int, int> arr[3];
    arr[0] = {1, 2};
    arr[1] = {2, 5};
    arr[2] = {3, 6};
    swap(arr[1], arr[0]);
    for (int i = 0; i < 3; i++)
    {
        cout << arr[i].first << " " << arr[i].second << endl;
    }
    return 0;
}
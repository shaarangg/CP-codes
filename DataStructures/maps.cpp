#include <bits/stdc++.h>
using namespace std;
void print(map<int, int> &d)
{
    map<int, int>::iterator itr;
    for (itr = d.begin(); itr != d.end(); itr++)
    {
        cout << itr->first << " " << itr->second << endl;
    }
}
// So, there are two types of maps in c++, ordered and unordered, ordered always returns key in accending order and implements trees to achieve the feat while unordered maps uses hashtables and return random keys when iterating through an iterator.

int main()
{
    map<int, int> d;
    // Ordered Maps
    d[1] = 5; // Here the time complexity is O(logn)
    d[3] = 10;
    d[6] = 0;
    d.insert({35, 77});
    print(d);
    // In order to check if a key exists or not
    auto it = d.find(25);
    if (it == d.end())
    {
        cout << "Not present" << endl;
    }

    // You can remove a key using iterator or key value
    d.erase(6); // time-complexity log(n)
    print(d);
    // For strings Time-complexity in ordered maps is size_of_string*log(n)

    // Unordered Maps
    // Here containers can't be a key it'll give a compilation error
    unordered_map<int, int> e;
    return 0;
}
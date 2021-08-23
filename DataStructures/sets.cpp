#include <bits/stdc++.h>
using namespace std;
template <class T>
void display(set<T> &s)
{
    for (auto i : s)
    {
        cout << i << " ";
    }
}
int main()
{
    // Just like maps sets in c++ are also of two types ordered sets and unorderd sets
    // Ordered set
    // Similary like ordered Map, sets also implement trees, hence the elements in the sets get's stored in a sorted order.
    // All the operations in the ordered set has a complexity of O(logN)
    set<string> s;
    s.insert("asdas");
    s.insert("sadsad");
    auto it = s.find("asdasd");
    if (it != s.end())
    {
        cout << "Found the element\n";
    }
    else
    {
        cout << "Couldn't find the element\n";
    }
    display(s);
    // Removing an element
    s.erase("sadsad");
    display(s);
    // Unordered sets
    // Using hash functions to store the values. Stores values in random order.
    // Time-complexity of all the operations is O(1)
    unordered_set<int> d;
    d.insert(1);
    d.insert(2);
    d.erase(1);
    return 0;
}
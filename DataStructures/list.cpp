#include <iostream>
#include <list>
using namespace std;
void display(list<int> &l)
{
    list<int>::iterator itr;
    cout << "Elements are :\n";
    for (itr = l.begin(); itr != l.end(); itr++)
    {
        cout << *itr << " ";
    }
    cout << '\n';
}
int main()
{
    // Adding elements to the list
    list<int> l1;
    l1.push_back(1);
    l1.push_back(2);
    l1.push_back(3);
    display(l1);

    // Removing elements from the list
    list<int> l2;
    l2.push_back(32);
    l2.push_back(54);
    l2.push_back(23);
    l2.push_back(433);
    l2.push_back(948);
    display(l2);
    l2.pop_back();
    display(l2);
    l2.pop_front();
    display(l2);
    l2.remove(23);
    display(l2);

    // Sorting the list
    list<int> l3;
    l3.push_back(32);
    l3.push_back(54);
    l3.push_back(23);
    l3.push_back(433);
    l3.push_back(948);
    display(l3);

    // Reversing a list
    list<int> l4;
    l4.push_back(32);
    l4.push_back(54);
    l4.push_back(23);
    l4.push_back(433);
    l4.push_back(948);
    display(l4);
    l4.reverse();
    display(l4);
    return 0;
}
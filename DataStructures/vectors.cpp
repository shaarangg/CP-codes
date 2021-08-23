#include <iostream>
#include <vector>
using namespace std;

template <class T>
void display(vector<T> &v)
{
    cout << "Elements are: \n";
    for (int i = 0; i < v.size(); i++)
    {
        cout << v[i] << endl;
    }
}
int main()
{
    // One Way of defininf vector
    // vector<int> vec1;
    // int size;
    // cout << "Enter size: ";
    // cin >> size;
    // int elem;
    // for (int i = 0; i < size; i++)
    // {
    //     cin >> elem;
    //     vec1.push_back(elem);
    // }
    // display(vec1);

    // Second way of defining vector
    // vector<char> vec2(4);
    // Initializes the vec2 with space 4 with garbage value
    // vec2.push_back('h');
    // display(vec2);

    // Third way
    // vector<char> vec3(vec2);
    // Copies vec2
    // display(vec3);

    // Fourth way
    vector<int> vec4(5, 0);
    // Creates a vector with length 5 will all values = 0
    display(vec4);

    // Iterator
    // An iterator is a pointer like object that points to an element inside the container. We can use the iterator to move inside the container.
    // vec4.begin() returns a iterator pointing to the first element in the vector
    vector<int>::iterator itr = vec4.begin();
    vec4.insert(itr + 4, 5);
    display(vec4);
    return 0;
}
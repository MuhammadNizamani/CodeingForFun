#include <iostream>
#include <vector>

using namespace std;
int main()
{
    vector<int> a;
    for (int i = 0; i <= 7; i++)
    {
        a.push_back(i);
    }
    cout << "print a array" << endl;
    for (auto i = a.cbegin(); i != a.cend(); ++i)
    {
        cout << *i << " " << endl;
    }

    return 0;
}
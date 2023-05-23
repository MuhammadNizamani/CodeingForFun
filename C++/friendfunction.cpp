// Data hiding is a fundamental concept of object-oriented programming. It
// restricts the access of private members from outside of the class.
// Similarly, protected members can only be accessed by derived classes and
// are inaccessible from outside. However, there is a feature in C++ called
// friend functions that break this rule and allow us to access member functions
// from outside the class.

#include <iostream>
using namespace std;
class Distance
{

private:
    int meter;
    friend int addFive(Distance);

public:
    Distance() : meter(0) {}
};

int addFive(Distance d)
{
    d.meter += 5;
    return d.meter;
}

int main()
{
    Distance d;
    cout << "Distance " << addFive(d);
    return 0;
}
#include <iostream>
using namespace std;
class Nam1
{

public:
    string name;
    int age;
    void name1()
    {
        cout << "My name is" << name
             << "and I am " << age
             << " years old" << endl;
    }
};

int main()
{
    string name = "Ishaque";
    int age = 23;
    cout << "trying C++ after longtime" << endl;
    Nam1 nameofperson;
    nameofperson.name = name;
    nameofperson.age = age;
    nameofperson.name1();
}

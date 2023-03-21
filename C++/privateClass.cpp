#include <iostream>
using namespace std;
class Person
{
private:
    string name;
    int age;
    string sex;

public:
    void intro(string n, int a, string s)
    {
        name = n;
        age = a;
        sex = s;
        cout << "My name is " << name << "my age is " << age << " and I am a " << sex << endl;
    }
};
int main()
{
    Person ishaque;
    ishaque.intro("Muhammad Ishaque", 25, "Male");

    return 0;
}
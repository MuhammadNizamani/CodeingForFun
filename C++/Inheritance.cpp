#include <iostream>
using namespace std;

class Person
{
public:
    string name;
    int age;
    string gender;

    void intro()
    {
        cout << "My name is" << name << "I am " << age << " year old and I am " << gender << endl;
    }
};

class Student : public Person
{
public:
    string schoolname;
    void schoolname1()
    {
        cout << "school name is " << schoolname << endl;
    }
};

int main()
{
    Student ishaque;
    ishaque.name = "Ishaque Nizamani";
    ishaque.age = 24;
    ishaque.gender = "Male";
    ishaque.schoolname = "MUET";

    ishaque.intro();
    ishaque.schoolname1();
}
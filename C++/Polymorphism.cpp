#include <iostream>
using namespace std;

class Animal
{
public:
    void animalSound()
    {
        cout << "The name makes sound" << endl;
    }
};
class Dog : public Animal
{
public:
    void animalSound()
    {
        cout << "The dog say : bow bow  " << endl;
    }
};
class Cat : public Animal
{
public:
    void animalSound()
    {
        cout << "The cat say : meeown meeown" << endl;
    }
};
int main()
{
    Animal animal;
    Dog dog;
    Cat cat;
    animal.animalSound();
    dog.animalSound();
    cat.animalSound();
}
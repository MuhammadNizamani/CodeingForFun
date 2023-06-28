#include<iostream>
using namespace std;
int main(){

int d,i,c = 0;
cout << "Enter a number: ";
cin >> d;
for(i = 1; i <= d; i++){

if((d % i) == 0){


    c++;
    }



}

if( c == 2)
    cout << d <<":is a prime number";
else
    cout << d <<":is not a prime number";

return 0;

}
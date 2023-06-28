#include<iostream>
using namespace std;
int main(){

int divisor, dividend, quotient,reminder;
cout << "Devidend: ";
cin >> dividend;

cout << "Divisor: ";
cin >> divisor;
quotient = dividend / divisor;
reminder = dividend % divisor;
cout << "Quotient = " << quotient <<endl ;
cout << "Reminder = " << reminder ;

// this code is different from this PR
return 0;



}

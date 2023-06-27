#include<iostream>
using namespace std;
int main(){
int num,num1,result=0;
cout << "Enter dividend: ";
cin >> num ;
cout << "Enter  divisor: ";
cin >> num1;

while(num>=num1){

  num=num -num1;

  result ++;


}

cout << "Division is: " << result;

return 0;


}



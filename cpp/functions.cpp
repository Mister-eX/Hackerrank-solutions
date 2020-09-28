#include<iostream> 
#include<algorithm> 
using namespace std; 
bool comp(int a, int b){
    return (a<b); /*for smallest elemnent a>b*/
}
int main() 
{ 
    cout << std::max({3, 4, 6,5}, comp)<<"\n"; 
  
return 0; 
}  
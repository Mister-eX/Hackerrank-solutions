#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    vector<int> arr;
    int size;
    cin>>size;
    int value;
    for(int i=0;i<size;i++)
    {
        cin>>value;
        arr.push_back(value);
    }
    sort(arr.begin(), arr.end());
    for(int i=0;i<size;i++)
    {
      cout<<arr[i]<<" ";
    }
    return 0;

}

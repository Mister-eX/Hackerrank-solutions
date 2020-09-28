#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 

    int n, q,k, which, index, val;
    cin>>n>>q;
    vector<vector<int>> list;
    for (int i=0; i<n; i++){
        cin>>k;
        vector<int> arr;
        for(int j= 0; j<k; j++){
            cin>>val;
            arr.push_back(val);
        }
        list.push_back(arr);
    }  

    for(int i= 0; i<q; i++){
        cin>>which>>index;
        cout<<list[which][index]<<endl;
    }
    return 0;
}
#include <bits/stdc++.h>


void update(int *a,int *b) {
    // Complete this function   
    int x= *a, y= *b;
    *a= abs(x+y);
    *b = abs(x-y);
}

int main() {
    int a, b;
    int *pa = &a, *pb = &b;
    
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
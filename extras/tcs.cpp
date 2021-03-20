#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    if(n<0) {
        cout<<"Wrong Input";
        return 0;
    }
    
    if((int)pow(n,4)%10 == n)cout<<"TRUE";
    else cout<<"FALSE";
    return 0;
}
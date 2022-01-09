//10870
#include <iostream>

using namespace std;
int arr[20];


int fivo(int n){
    if(n>=2){
        return fivo(n-1)+fivo(n-2);
    }else if(n==1) {
        return 1;
    }else if(n==0){
        return 0;
    }
    
    return -1;
}

int main()
{

    int n=0;
    cin>>n;
    cout<<fivo(n);
    


    return 0;
}
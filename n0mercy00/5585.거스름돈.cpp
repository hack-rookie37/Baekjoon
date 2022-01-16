//5585


#include <iostream>

using namespace std;

int main()
{
    //들어온 돈
    int taro=0;
    //잔돈별 갯수
    int fh=0,h=0,ff=0,t=0,f=0,o=0;
    int temp=0; 
    
    cin>>taro;
    temp=1000-taro;
    
    
    fh=temp/500;
    temp = temp%500;
    
    
    h=temp/100;
    temp = temp%100;
    
    
    ff=temp/50;
    temp = temp%50;
   
    
    t=temp/10;
    temp = temp%10;
    
    
    f=temp/5;
    temp = temp%5;
    
    
    o=temp/1;
    temp = temp%1;
   
    
    cout<<fh+h+ff+t+f+o;
    
    

    return 0;
}
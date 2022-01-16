//제출본
#include <iostream>
#include <algorithm>
using namespace std;
int town[330][330];
int INDEX=0;
int array12[330];
int n=0;
int Cheack(int i, int j,bool root){

    if(town[i][j]==1){
        town[i][j]=2;
        array12[INDEX]++;
        if(i-1>=0){
            Cheack(i-1,j,false);
        }
        if(j+1<n){
            Cheack(i,j+1,false);
        }
        if(i+1<n){
            Cheack(i+1,j,false);
        }
        if(j-1>=0){
            Cheack(i,j-1,false);
        }
       if(root==true){
         INDEX++;  
       }
        return town[i][j];
        
    }else{
        return 0;
    }
}

int main()
{
    cin>>n;
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%1d",&town[i][j]);
        }   
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            Cheack(i,j,true);
        }
    }
    sort(array12,array12+INDEX);
    cout<<INDEX<<"\n";
    for(int i=0;i<INDEX;i++){
        cout<<array12[i]<<"\n";
    }
    return 0;
}